from bs4 import BeautifulSoup

def get_board(table_html):
    soup = BeautifulSoup(table_html, 'html.parser')
    table = soup.find('table', attrs={'class':'t'})
    
    board = []
    for row in table.find_all('tr'):
        row_data = []
        for cell in row.find_all('input'):
            value = cell.get('value')
            if value is None:
                value = '.'
            row_data.append(value)
        board.append(row_data)
    
    return board
