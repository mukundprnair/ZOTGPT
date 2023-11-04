from bs4 import BeautifulSoup
import requests


class InvalidProfessorName(Exception):
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return self.text

class Parser():
    def __init__(self, prof_name):
        self.name = prof_name
        self.BASE_URL = "https://ics.uci.edu/people/?term="

    def return_blurb(self):
        prof_page = self.get_prof_page(self.get_search_page())
        return self.get_blurb(prof_page)

    def _encoded(self, name: str) -> str:
        return name.replace(" ", "+")

    def get_beautiful_soup(self, url: str) -> BeautifulSoup:
        response = requests.get(url)
        html = response.text
        return BeautifulSoup(html, 'html.parser')

    def get_search_page(self) -> BeautifulSoup:
        return self.get_beautiful_soup(self.BASE_URL+self._encoded(self.name))
        

    def get_prof_page(self, bs: BeautifulSoup) -> BeautifulSoup:
        a_tags = bs.find_all('a', class_="item__link")
        for i in range(len(a_tags)):
            # this is the span underneath the a_tag
            contents = a_tags[i].contents
            # compares the inner text of the span after stripping and lowering
            if contents[1].text[5:].strip().lower() == self.name.lower():
                url_to_use = a_tags[i]['href']
                return self.get_beautiful_soup(url_to_use)
        raise InvalidProfessorName("That professor name was not found on the website!")

        
    def get_blurb(self, bs: BeautifulSoup) -> str:
        # if it has this div they have a blurb

        div_element = bs.find('div', class_ = 'post__content-inner t-content l-container__stagger-double')
        # print("Out div element")
        # print(div_element)
        prof_info = ""
        if div_element is not None:
            # print("Our p element")
            p_element = div_element.find_all("p")

            for para in p_element:
                prof_info += para.text

        return prof_info


if __name__ == "__main__":
    p = Parser("Iftekhar Ahmed")
    print(p.return_blurb())

    '''
    url = "https://ics.uci.edu/people/sangeetha-jyothi/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    p.get_blurb(soup)
    '''


