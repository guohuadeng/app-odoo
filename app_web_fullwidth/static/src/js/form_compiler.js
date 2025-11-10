/** @odoo-module **/
import { FormCompiler } from "@web/views/form/form_compiler";
import { patch } from "@web/core/utils/patch";

patch(FormCompiler.prototype, {
    compileForm(el, params) {
        const res = super.compileForm(el, params);
        if (odoo.web_chatter_position === "sided") {
            const classes = res.getAttribute("t-attf-class");
            const newClasses = classes.replace('{{ __comp__.uiService.size < 6 ? "flex-column" : "flex-nowrap h-100" }}', 'flex-nowrap h-100')
            res.setAttribute("t-attf-class", `${newClasses}`);
            return res;
        }

        else if (odoo.web_chatter_position === "bottom") {
            const classes = res.getAttribute("t-attf-class");
            const formView = res.getElementsByClassName('o_form_sheet_bg')[0];

            if (formView) {
                formView.classList.add('customBottom');
                const formParent = formView.parentElement;

                if (formParent) {
                    const chatter = formParent.querySelector('.o-mail-Form-chatter');
                    if (chatter) {
                        chatter.classList.add('customBottom');
                    }
                }

                const newClasses = classes.replace('{{ __comp__.uiService.size < 6 ? "flex-column" : "flex-nowrap h-100" }}', 'flex-column');
                res.setAttribute("t-attf-class", `${newClasses}`);
            }

            return res;
        }

        return res;
    },

    compile(node, params) {
        const res = super.compile(node, params);

        const chatterContainerHookXml = res.querySelector(".o-mail-Form-chatter");
        if (!chatterContainerHookXml) {
            return res; // no chatter, keep the result as it is
        }

        if (odoo.web_chatter_position === "sided") {
            const classes = chatterContainerHookXml.getAttribute("t-attf-class")
            if(classes){
                const newClasses = classes.replace('{{ __comp__.uiService.size >= 6 ? "o-aside" : "mt-4 mt-md-0" }}', 'o-aside')
                res.setAttribute("t-attf-class", `${newClasses}`);
            }
            return res
        }
        else if (odoo.web_chatter_position === "bottom") {
            const classes = chatterContainerHookXml.getAttribute("t-attf-class")
            if(classes){
                const newClasses = classes.replace('{{ __comp__.uiService.size >= 6 ? "o-aside" : "mt-4 mt-md-0" }}', 'mt-4 mt-md-0')
                res.setAttribute("t-attf-class", `${newClasses}`);
            }
            return res
        }
        return res;
    },
});

