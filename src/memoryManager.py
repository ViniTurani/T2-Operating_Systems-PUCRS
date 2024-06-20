import random

class MemoryManager:
    def __init__(self, virtual_memory_bits, physical_memory_bits, page_size_bits):
        self.virtual_memory_bits = virtual_memory_bits
        self.physical_memory_bits = physical_memory_bits
        self.page_size_bits = page_size_bits
        
        # Calcula o número de páginas e molduras
        self.num_pages = 2 ** (self.virtual_memory_bits - self.page_size_bits)
        self.num_frames = 2 ** (self.physical_memory_bits - self.page_size_bits)
        
        # Estruturas de dados
        self.page_table = [-1] * self.num_pages  # Tabela de páginas inicializada com -1
        self.physical_memory = [0] * self.num_frames  # Memória física inicializada com 0

    def get_page_number(self, virtual_address):
        """Retorna o número da página a partir do endereço virtual."""
        return virtual_address >> self.page_size_bits

    def get_offset(self, virtual_address):
        """Retorna o offset dentro da página a partir do endereço virtual."""
        return virtual_address & ((1 << self.page_size_bits) - 1)

    def allocate_frame(self, page_number):
        """Aloca uma moldura para a página especificada, se houver espaço."""
        for frame_number, frame in enumerate(self.physical_memory):
            if frame == 0:  # Moldura livre encontrada
                self.physical_memory[frame_number] = 1  # Marca a moldura como usada
                self.page_table[page_number] = frame_number  # Atualiza a tabela de páginas
                return frame_number
        return None  # Não há espaço na memória física

    def virtual_to_physical(self, virtual_address):
        """Converte um endereço virtual em um endereço físico."""
        page_number = self.get_page_number(virtual_address)
        offset = self.get_offset(virtual_address)
        
        frame_number = self.page_table[page_number]
        if frame_number == -1:  # Página não está na memória física
            frame_number = self.allocate_frame(page_number)
            if frame_number is None:
                raise MemoryError("Memória física lotada")
        
        physical_address = (frame_number << self.page_size_bits) | offset
        return physical_address

    def simulate(self):
        """Executa a simulação de mapeamento de endereços virtuais para físicos."""
        try:
            for _ in range(100):  # Gera 100 endereços virtuais aleatórios
                virtual_address = random.randint(0, 2**self.virtual_memory_bits - 1)
                physical_address = self.virtual_to_physical(virtual_address)
                print(f"Endereço virtual: {virtual_address}, Endereço físico: {physical_address}")
        except MemoryError as e:
            print(e)
            print("Simulação interrompida: memória física lotada.")

