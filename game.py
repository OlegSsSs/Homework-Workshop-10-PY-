import enum
from random import randint


class Order(enum.Enum):
    '''кто ходит'''
    player = 0
    cpu = 1


class Game:
    '''
    Игра крестики - нолики
    
    '''
    help = ('Игра крестики - нолики.\n')

    matrix: list  # Игровое поле
    gamestatus: bool  # состояние игры

    def __init__(self):
        self.gamestatus = False
        '''начальное состояние игры (остановлена)'''
        self.matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        '''Игровое поле'''
        self.act = Order.player
        '''чей ход: cpu/player'''

    def start(self):
        """старт игры
        """
        self.gamestatus = True
        self.matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def stop(self):
        """остановка игры
        """
        self.gamestatus = False

    def action_player(self, num_position):
        """ход игрока
        Args:
            num_position (int): номер позиции в игровом поле, куда игрок поставил знак "Х"
        """
        if self.gamestatus:

            # игрок сделал ход
            if (self.matrix[num_position-1] != 'X') and (self.matrix[num_position-1] != 'O'):
                self.matrix[num_position-1] = 'X'
                return
        else:
            pass

  

    def action_cpu(self):
        """ход компьютера
        Returns:
            int : позиция, на которую компьютер поставил знак "О"
        """
        if self.gamestatus:
            for i in range(0,len(self.matrix)):
                i = randint(0, 8)
                if (self.matrix[i] != 'X') and self.matrix[i] != 'O':
                    self.matrix[i] = 'O'
                    return
        else:
            return 0


    def check_game_state(self):
        """Проверка победителя"""
        if self.matrix[0] == self.matrix[1] == self.matrix[2]:
            print(f'Победили {self.matrix[0]}')
            return True
        elif self.matrix[3] == self.matrix[4] == self.matrix[5]:
            print(f'Победили {self.matrix[3]}')
            return True
        elif self.matrix[6] == self.matrix[7] == self.matrix[8]:
            print(f'Победили {self.matrix[6]}')
            return True
        elif self.matrix[0] == self.matrix[3] == self.matrix[6]:
            print(f'Победили {self.matrix[0]}')
            return True
        elif self.matrix[1] == self.matrix[4] == self.matrix[7]:
            print(f'Победили {self.matrix[1]}')
            return True
        elif self.matrix[2] == self.matrix[5] == self.matrix[8]:
            print(f'Победили {self.matrix[2]}')
            return True
        elif self.matrix[0] == self.matrix[4] == self.matrix[8]:
            print(f'Победили {self.matrix[0]}')
            return True
        elif self.matrix[2] == self.matrix[4] == self.matrix[6]:
            print(f'Победили {self.matrix[2]}')
            return True
        else: return False
    

    def check_drawn_game(self):
        """Проверка ничьей"""
        if len(set(self.matrix)) == 2:
            return True



    def showMatrix(self):
        return f'{self.matrix[0]} | {self.matrix[1]} | {self.matrix[2]} \n{self.matrix[3]} | {self.matrix[4]} | {self.matrix[5]} \n{self.matrix[6]} | {self.matrix[7]} | {self.matrix[8]} \n'
    
