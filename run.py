from pprint import pprint as pp

import justext

HTML_TAGS = u'h1 h2 h3 h4 h5 h6 strong b em i p div span'.split(' ')
weights = {html_tag: len(HTML_TAGS) - weight for weight, html_tag in
           enumerate(HTML_TAGS)}
tag_soup = []


def main():
    with open('content.html') as htmlfile:
        content = htmlfile.read()
        paragraphs = justext.justext(content, justext.get_stoplist("English"))
        for paragraph in paragraphs:
            #  if not paragraph.is_boilerplate:
            tag = paragraph.dom_path.rsplit('.')
            tag_soup.append(
                {
                    'paragraph': paragraph,
                    'tag': tag[-1],
                    'weight': weights.get(tag[-1], 0),  # highest
                    'dom_path': paragraph.dom_path,
                    'dom_path_len': len(tag),  # shortest
                    'words_count': paragraph.words_count,  # longest
                    'text': paragraph.text,  # longest
                }
            )
        [pp(para) for para in tag_soup]
        ordered_tag_soup = sorted(tag_soup, key=lambda p:
            (-p['weight'], p['dom_path_len'], -p['words_count'], -len(p['text']))
        )
        print(30 * '-')
        [pp(para) for para in ordered_tag_soup]


if __name__ == '__main__':
    main()
