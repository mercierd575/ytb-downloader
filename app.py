#author: mercierd575
#v0.4.0

import streamlit as st          # Using streamlit for the WebApp

st.set_page_config(
    page_title="YouTube Downloader (Offline)",  # Name displayed on tab
    page_icon="⚠️",  # Use an emoji or a path to an image for the tab icon
    layout="centered",  # "centered" or "wide"
    initial_sidebar_state="auto"  # "auto", "expanded" or "collapsed"
)

st.title("Service Offline Indefinitely")    # Title of the web app

st.markdown("""
### Why is this offline?

YouTube has recently introduced stricter technical restrictions that prevent
reliable video downloads without user authentication and browser-level access.

To protect users and avoid unsafe or misleading behavior, this service has been
**intentionally taken offline**

*Fighting against YouTube's technical restrictions has become increasingly
difficult. The platform continuously updates its systems to prevent automated
downloads, requiring user authentication, browser-level interactions, and
frequent workarounds. Each change can break existing tools, and what worked
yesterday may fail today. Maintaining a downloader that works reliably across
all videos now requires complex setups, constant updates, and handling sensitive
user credentials; making it impractical and potentially unsafe for public use.
I would never want to knowingly make available a tool that is unsafe to the
public.*

---

### What does this mean?

- No downloads at the moment
- No URL processing
- No background work happening

---

### Will it come back?

Possibly. If YouTube changes their policies or a safe, user-friendly solution
becomes available, this service may return.

---

### What can I do now?

- If you are not tech-savvy enough to run an app locally, you could use
[EzConv](https://ezconv.cc), which is updated often enough to be reliable.
- If you are a tech-savvy person, you could try to run the latest version
of [my app](https://github.com/mercierd575/ytb-downloader) locally
on your computer or local network.

---

Thank you for your understanding.
""")

st.markdown("---")
st.caption(
    "Version 0.4.0 - Service Offline"
)
