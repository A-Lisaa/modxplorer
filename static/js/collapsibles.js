function showElementsById(elements, ids) {
    elements.forEach((element) => {
        let id = element.id.split("-")[1]; 
        if (id in ids) {
            return new bootstrap.Collapse(element);
        }
    });
}

function showElementsFromClassAndCookieName(elementsClassName, cookieName) {
    let shownElementsCookie = Cookies.get(cookieName);
    if (!shownElementsCookie) {
        return;
    }
    let shownElements = shownElementsCookie.split(";");
    let elements = [...document.getElementsByClassName(elementsClassName)];
    showElementsById(elements, shownElements);
}

function restoreSubelements() {
    showElementsFromClassAndCookieName("mod-subelements", "shownMods");
    showElementsFromClassAndCookieName("mod-subelements", "shownFolders");
    showElementsFromClassAndCookieName("folder-subelements", "shownMods");
    showElementsFromClassAndCookieName("folder-subelements", "shownFolders");
}

function saveModpackSubelementsState(subelements, cookieName) {
    let cookieText = "";
    subelements.forEach((subelement) => {
        if (subelement.classList.contains("show")) {
            let id = subelement.id.split("-")[1];
            cookieText += id + ";";
        }
    });
    Cookies.set(cookieName, cookieText, { sameSite: "Lax" });
}

function saveSubelements() {
    saveModpackSubelementsState([...document.getElementsByClassName("mod-subelements")], "shownMods");
    saveModpackSubelementsState([...document.getElementsByClassName("folder-subelements")], "shownFolders");
}

window.addEventListener("DOMContentLoaded", () => {
    restoreSubelements();
});