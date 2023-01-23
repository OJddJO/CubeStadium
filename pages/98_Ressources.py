import streamlit as st
from PIL import Image

icon = Image.open("icon.png")
st.set_page_config(page_title="Ressources", page_icon=icon)
st.title("Ressources")
st.sidebar.markdown("**Made with ❤️ by** [***OJddJO***](https://github.com/OJddJO/)")

algo = st.expander("Algorithmes")
algo.subheader("3x3x3")
algo.caption("- F2L: https://jperm.net/3x3/cfop/f2l")
algo.caption("- OLL: https://jperm.net/algs/oll")
algo.caption("- PLL: https://jperm.net/algs/pll")
algo.caption("- COLL: https://jperm.net/algs/coll")
algo.caption("- Winter Variation: https://jperm.net/algs/wv")
algo.caption("- Advanced F2L PDF: https://drive.google.com/file/d/1nzAXYUWZJ6H2wIOXaHdWXep3W57tArbR/view")
algo.caption("- CubeHead PLL PDF: https://drive.google.com/file/d/1JM798XJ1FlpRF-8oGlil8l2-57axbMXn/view")

others = st.expander("Others")
others.subheader("3x3x3")
others.caption("- 2-Sided PLL Recognition: https://logiqx.github.io/cubing-algs/html/2spll.html")
others.caption("- PLL Trainer: https://speedcubedb.com/t/pllrecog")
