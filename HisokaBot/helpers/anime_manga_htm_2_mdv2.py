def anime_manga_html_2_mdv2(caption, a_m_id):
    caption = caption = caption.replace('<b>', '*').replace('</b>', '*'). \
        replace('<pre>', '`').replace('</pre>', '`'). \
        replace('<i>', '').replace('</i>', ''). \
        replace('<br>', '\n').replace('.', '\\.'). \
        replace('(', '\\(').replace(')', '\\)'). \
        replace(f"\(https://img\.anili\.st/media/{a_m_id}\)",
                f"(https://img\.anili\.st/media/{a_m_id})"). \
        replace("None", "").replace("-", "\-").replace('!', '\!').replace('+','\\+')
    return caption
