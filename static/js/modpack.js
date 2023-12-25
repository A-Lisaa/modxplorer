function createModpackAsyncModalForm(element, formURL, dataUrl, reinstantiationFunction) {
    modalForm(
        element,
        {
            formURL: formURL,
            // TODO: asyncUpdate doesn't fucking work
            // asyncUpdate: true,
            // asyncSettings: {
            //     closeOnSubmit: true,
            //     successMessage: "<p>Success</p>",
            //     dataUrl: dataUrl,
            //     dataElementId: "#content-list",
            //     dataKey: "content_list",
            //     addModalFormFunction: reinstantiationFunction
            // }
        }
    );
}

function createModpackAsyncModalForms(elements, dataUrl, reinstantiationFunction) {
    elements.forEach(
        (element) => {
            let formUrl = element.getAttribute("form-url");
            if (!formUrl) {
                console.warn("No form url specified for element: " + element);
                return;
            }
            createModpackAsyncModalForm(
                element,
                formUrl,
                dataUrl,
                reinstantiationFunction
            );
        }
    );
}