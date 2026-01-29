from odoo import http
from odoo.http import request
import json
from datetime import datetime, timedelta

class StockMarketController(http.Controller):
    """
    股票市场数据控制器 - 处理前端请求和数据展示
    """
    
    @http.route('/stock/market/data', type='json', auth='user', methods=['POST'], csrf=False)
    def get_stock_data(self, stock_code, days=30, **kwargs):
        """
        获取股票数据用于图表展示
        :param stock_code: 股票代码
        :param days: 查询天数
        """
        try:
            stock_model = request.env['stock.market.data']
            chart_data = stock_model.get_chart_data(stock_code, days)
            
            return {
                'success': True,
                'data': chart_data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    @http.route('/stock/market/dashboard', type='http', auth='user', website=True)
    def stock_dashboard(self, **kwargs):
        """
        股票数据分析仪表板页面
        """
        # 获取最近的股票数据
        stock_data = request.env['stock.market.data'].search([], limit=50, order='trade_date desc')
        
        # 获取系统配置的监控股票列表
        stock_list_str = request.env['ir.config_parameter'].sudo().get_param('stock.monitor.list', '')
        stock_list = [stock.strip() for stock in stock_list_str.split(',') if stock.strip()]
        
        return request.render('app_odoo_customize.stock_market_dashboard', {
            'stock_data': stock_data,
            'stock_list': stock_list,
            'title': '中国股票市场数据监控'
        })

    @http.route('/stock/market/fetch', type='json', auth='user', methods=['POST'], csrf=False)
    def fetch_single_stock(self, stock_code, **kwargs):
        """
        手动获取单个股票数据
        :param stock_code: 股票代码
        """
        try:
            stock_model = request.env['stock.market.data']
            stock_model.fetch_stock_data(stock_code)
            
            return {
                'success': True,
                'message': f'股票 {stock_code} 数据采集完成'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    @http.route('/stock/market/buy_signals', type='json', auth='user')
    def get_buy_signals(self, **kwargs):
        """
        获取买入信号
        """
        try:
            buy_signals = request.env['stock.market.data'].search([
                ('buy_signal', '=', True)
            ], limit=20, order='trade_date desc')
            
            signals_data = []
            for signal in buy_signals:
                signals_data.append({
                    'stock_code': signal.stock_code,
                    'stock_name': signal.stock_name,
                    'trade_date': signal.trade_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'price': signal.close_price,
                    'wave_level': signal.wave_theory_level
                })
            
            return {
                'success': True,
                'signals': signals_data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }