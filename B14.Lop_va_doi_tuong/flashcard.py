import random



class Flashcard:
    def __init__(self):
        self.animals = {'Con ong': 'bee',
                        'Con thỏ': 'rabbit',
                        'Con cua': 'crab',
                        'Con mèo': 'cat',
                        'Con ngựa': 'horse',
                        'Con khỉ': 'monkey',
                        'Con lừa': 'donkey',
                        'Con hổ': 'tiger',
                        'Con sư tử': 'lion',
                        'Con cá': 'fish',
                        'Con chó': 'dog'}
    def quiz(self):
        count = 0
        for i in range(5):
            random_word = random.choice(list(self.animals.keys()))
            print("Lượt chơi: ", i)
            print(random_word)
            input_word = input("Bạn hãy nhập từ tiếng Anh tương ứng: ")
            if input_word.strip().lower() == self.animals[random_word]:
                print("Bạn đã nhập đúng òi")
                count += 1
            else:
                print("Bạn đã nhập sai òi")
        print("Bạn đã đúng {} trên {}".format(count, 5))
        
flashcard = Flashcard()
flashcard.quiz()