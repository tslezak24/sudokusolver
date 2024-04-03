from bs4 import BeautifulSoup

def file_in():
    html = open("boardhtml.txt", "r").read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('table', attrs={'class':'t'}), soup

def file_out(output):
    file = open("completedboard.txt", "w")
    file.write(output)
    return True

def get_board():
    table = file_in() 
    board = []
    for row in table[0].find_all('tr'):
        row_data = []
        for cell in row.find_all('input'):
            value = cell.get('value')
            if value is None:
                value = '.'
            row_data.append(value)
        board.append(row_data)
    
    return board

def update_board(board):
    table = file_in()

    for r, row in enumerate(table[0].find_all('tr')):
        for c, cell in enumerate(row.find_all('input')):
            cell['value'] = board[r][c]
    return file_out(str(table[1]))