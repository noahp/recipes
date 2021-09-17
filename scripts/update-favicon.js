// sorry about how crappy this is :(

// get the 3rd glyph in the main content and paste it into the favicon field
let main_content = document.getElementById("main-content");

let emoji = "🥘";

for (let i = 0; i < main_content.children.length; i++) {
  let child = main_content.children[i];
  if (child.tagName == "H1") {
    let glyphs = Array.from(child.children[0].text);
    emoji = glyphs[0];
    break;
  }
}

let elem = document.getElementById("favicon");
let icon_href = `data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>${emoji}</text></svg>`;

elem.setAttribute("href", icon_href);
