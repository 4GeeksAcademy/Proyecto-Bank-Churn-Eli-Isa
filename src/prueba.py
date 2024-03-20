import streamlit as st
import reveal_slides as rs

url_imagen='/workspaces/Proyecto-Bank-Churn-Eli-Isa/src/DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/Sin-título-1.jpg'
sample_markdown = r"""
# Reveal.js + Streamlit
Add <a target="_blank" href="https://revealjs.com/">Reveal.js</a> presentations to your Streamlit app.
---
## Installation
`pip install streamlit-reveal-slides`

\[[GitHub](https://github.com/bouzidanas/streamlit.io/tree/7748c2a97f4ca54ce4b8120a054d6c66e8be296d/streamlit-reveal-slides)\] \[[PyPI](https://pypi.org/project/streamlit-reveal-slides/)\]
---
## Presentation Features
- Create slides from markdown or markup <!-- .element: class="fragment" data-fragment-index="0" -->
- Touch, mouse, and keyboard navigation <!-- .element: class="fragment" data-fragment-index="1" -->
- Fullscreen and overview modes <!-- .element: class="fragment" data-fragment-index="2" -->
- Search and Zoom (plugins) <!-- .element: class="fragment" data-fragment-index="3" -->
- Display LaTeX and syntax highlighted code (plugins) <!-- .element: class="fragment" data-fragment-index="4" -->
---
## Slide Content Creation
![Image]({url_imagen})

A paragraph with some text and a markdown [link](https://hakim.se). 
Markdown links get displayed within the parent iframe.
--
Another paragraph containing the same <a target="_blank" href="https://hakim.se">link</a>.
However, this link will open in a new tab instead. 
This is done using an HTML `<a>` tag with `target="_blank"`.
---
"""
st.markdown("## STREAMLIT REVEAL.JS COMPONENT")
with st.sidebar:
    st.header("Component Parameters")
    theme = st.selectbox("Theme", ["black", "black-contrast", "blood", "dracula", "moon", "white", "white-contrast", "league", "beige", "sky", "night", "serif", "simple", "solarized"])
    height = st.number_input("Height", value=500)
    st.subheader("Slide Configuration")
    content_height = st.number_input("Content Height", value=900)
    content_width = st.number_input("Content Width", value=900)
    scale_range = st.slider("Scale Range", min_value=0.0, max_value=5.0, value=[0.1, 3.0], step=0.1)
    margin = st.slider("Margin", min_value=0.0, max_value=0.8, value=0.1, step=0.05)
    plugins = st.multiselect("Plugins", ["highlight", "katex", "mathjax2", "mathjax3", "notes", "search", "zoom"], [])
    st.subheader("Initial State")
    hslidePos = st.number_input("Horizontal Slide Position", value=0)
    vslidePos = st.number_input("Vertical Slide Position", value=0)
    fragPos = st.number_input("Fragment Position", value=-1)
    overview = st.checkbox("Show Overview", value=False)
    paused = st.checkbox("Pause", value=False)
    
# Add the streamlit-reveal-slide component to the Streamlit app.                    
currState = rs.slides(sample_markdown, 
                    height=height, 
                    theme=theme, 
                    config={
                            "width": content_width, 
                            "height": content_height, 
                            "minScale": scale_range[0], 
                            "center": True, 
                            "maxScale": scale_range[1], 
                            "margin": margin, 
                            "plugins": plugins
                            }, 
                    initial_state={
                                    "indexh": hslidePos, 
                                    "indexv": vslidePos, 
                                    "indexf": fragPos, 
                                    "paused": paused, 
                                    "overview": overview 
                                    }, 
                    markdown_props={"data-separator-vertical":"^--$"}, 
                    key="foo")

if currState["indexh"] == 0:
    st.markdown("Reveal.js is an open source HTML presentation framework. It enables anyone with a web browser to create fully-featured and beautiful presentations for free. \n\nThe framework comes with a broad range of features including nested slides, Markdown support, Auto-Animate, PDF export, speaker notes, LaTeX support and syntax highlighted code.")
elif currState["indexh"] == 2:
    if currState["indexf"] == 0:
        st.markdown("_(see later slides for details and examples)_")
    elif currState["indexf"] == 1:
        st.markdown("- You can swipe horizontally or vertically to navigate through a presentation on any touch-enabled device. \n- You can use the `space` or arrow keys on your keyboard to navigate as well. Press `Shift` + `/` to see all keyboard shortcuts. \n- Navigating with the mouse is as simple as clicking the directional arrows near the edges or corners of the slides.")
    elif currState["indexf"] == 2:
        st.markdown("- Press the `F` key on your keyboard to enter full-screen presentation mode. Press `ESC` to exit full-screen mode. \n- Press the `O` of `ESC` key to enter and exit overview mode")
    elif currState["indexf"] == 3:
        st.write(":arrow_left: Make sure to add the search and zoom plugins to activate these features.")
        st.markdown("- Press `Ctrl` + `Shift` + `F` keys on your keyboard to open and close the search dialog. \n- Press the `Alt` key and right click to zoom in and out on the region the mouse is hovering over.")
    elif currState["indexf"] == 4:
        st.markdown("_(see later slides for details and examples)_")
elif currState["indexh"] == 3:
    st.markdown('''This component allows for two ways of creating reveal.js presentations. \n1. [Markdown](https://revealjs.com/markdown/) \n2. [Markup](https://revealjs.com/markup/) \n\nThe primary way is using markdown. By default, the component `slide` function accepts a string containing markdown as input. Note that this streamlit component takes care of the html tags (`<section>`, `<textarea>`, `<script>`) for you so you only have to worry about the markdown content. The following is simple example of markdown for a presentation with three slides: ''')
    sample_markdown = '''## Slide 1
    A paragraph with some text and a [link](https://hakim.se).
---
## Slide 2
---
## Slide 3'''

# Mostrar la imagen con st.image()
st.image(url_imagen, caption="Imagen desde el repositorio", use_column_width=True)