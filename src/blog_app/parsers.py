import datetime
import re
from html import escape as escape_html
import bs4
import misaka

from .settings import SETTINGS

class Helper():
    @classmethod
    def striptags(cls, html):
        return ''.join(cls.parse(html).findAll(text=True))

    @staticmethod
    def parse(html):
        return bs4.BeautifulSoup(html, SETTINGS.get('BS4_PARSER'))


class BlogHtmlRenderer(misaka.HtmlRenderer):
    @staticmethod
    def block_code(code, language):
        html = "<pre><code"
        html += " data-language=\"{0}\">".format(language) if language else ">"
        html += escape_html(code)
        html += "</code></pre>"
        return html


class BlogParser():

    EXCERPT_MAX_LENGTH = 600

    def extractfilemeta(self, filepath):
        with open(filepath, 'r') as file:
            content = file.read()

        return self.extractmeta(content)

    def extractmeta(self, text):
        parts = re.split('-{4}', text)
        meta = parts[1].strip()
        content = "----".join(parts[2:]).strip()

        meta_matches = re.findall(self.meta_pattern, meta)
        final_meta = {}

        for key, val in meta_matches:
            if key == 'create_date':
                val = datetime.datetime.strptime(val.strip(), '%Y-%m-%d').date()
            else:
                val = val.strip()

            final_meta[key] = val

        content = self.parse_content(content)
        final_meta['excerpt'] = self.make_excerpt(content)
        final_meta['excerpt_nohtml'] = Helper.striptags(final_meta['excerpt'])

        return [final_meta, content]

    @staticmethod
    def parse_content(content):
        return misaka.Markdown(BlogHtmlRenderer(), extensions=('fenced-code',))(content)

    @staticmethod
    def make_excerpt(content):
        soup = Helper.parse(content)

        paragraph = soup.p
        if paragraph is None:
            return content

        excerpt = [paragraph.renderContents()]
        next_sibling = None
        next_element = paragraph

        while next_sibling is None:
            next_element = next_element.nextSibling

            # BeautifulSoup was returning newline characters as the next sibling,
            # we want to discard those...
            if not isinstance(next_element, bs4.element.Tag):
                continue

            validtag = next_element.name.lower() == 'p'
            next_sibling = next_element if validtag else False

        if next_sibling:
            excerpt.append(next_sibling.renderContents())

        return "\n".join('<p>{0}</p>'.format(p.decode('utf-8')) for p in excerpt)

    @property
    def meta_pattern(self):
        return re.compile(r'([\w]+):(.+)', re.M)
