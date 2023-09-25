# Implemente uma lista circular com nomes de músicas a qual tenha as seguintes características:
# Alocação de memória dinâmica para as músicas inseridas
# Uma função de busca de músicas por nomes
# Contagem da quantidade de músicas presentes na lista
# Remoção de músicas
# Adição de músicas
# A última música aponta para a primeira música da lista.

class Node:
    def __init__(self, music):
        self.music = music
        self.next = None

class CircularMusicList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_song(self, music):
        new_node = Node(music)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove_song(self, music):
        if self.head is None:
            return

        current = self.head
        prev = None
        found = False

        while True:
            if current.music == music:
                found = True
                break

            if current.next == self.head:
                break

            prev = current
            current = current.next

        if found:
            if self.size == 1:
                self.head = None
                self.tail = None
            elif current == self.head:
                self.head = current.next
                self.tail.next = self.head
            elif current == self.tail:
                self.tail = prev
                self.tail.next = self.head
            else:
                prev.next = current.next
            self.size -= 1
        else:
            print(f"A música '{music}' não foi encontrada na lista.")

    def search_song(self, music):
        if self.head is None:
            return None

        current = self.head

        while True:
            if current.music == music:
                return current
            if current.next == self.head:
                break
            current = current.next

        return None

    def count_songs(self):
        return self.size

    def display(self):
        if self.head is None:
            return

        current = self.head

        while True:
            print(current.music, end=" -> ")
            if current.next == self.head:
                break
            current = current.next

        print()
# Exemplo de uso:
if __name__ == "__main__":
    music_list = CircularMusicList()
    music_list.add_song("Bem mais que tudo")
    music_list.add_song("Pra que")
    music_list.add_song("Dependo de ti")
    music_list.add_song("Me ajude a melhorar")

    print("Lista de Músicas:")
    music_list.display()

    print(f"Quantidade de Músicas na Lista: {music_list.count_songs()}")

    search_result = music_list.search_song("Dependo de ti")
    if search_result:
        print(f"A música '{search_result.music}' foi encontrada.")
    else:
        print("A música não foi encontrada.")

    music_list.remove_song("Me ajude a melhorar")

    print("Lista de Músicas após a remoção:")
    music_list.display()

    print(f"Quantidade de Músicas na Lista após a remoção: {music_list.count_songs()}")
