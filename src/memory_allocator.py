# memory_allocator.py

class MemoryAllocator:
    def __init__(self, virtual_memory_bits, physical_memory_bits, page_size_bits):
        self.virtual_memory_bits = virtual_memory_bits
        self.physical_memory_bits = physical_memory_bits
        self.page_size_bits = page_size_bits

        
        self.NUM_PAGES = 2 ** (self.virtual_memory_bits - self.page_size_bits)
        self.NUM_FRAMES = 2 ** (self.physical_memory_bits - self.page_size_bits)
        self.page_table = [-1] * self.NUM_PAGES
        self.physical_memory = [0] * self.NUM_FRAMES

    def translate_address(self, virtual_address):
        if virtual_address >= 2**self.virtual_memory_bits:
            raise ValueError("Endereço virtual fora do limite.")
        
        page_number = virtual_address >> self.page_size_bits
        offset = virtual_address & ((1 << self.page_size_bits) - 1)
        
        if self.page_table[page_number] == -1:
            try:
                free_frame = self.physical_memory.index(0)
            except ValueError:
                raise MemoryError("Memória física está cheia. Não é possível continuar.")
            
            self.page_table[page_number] = free_frame
            self.physical_memory[free_frame] = 1
        
        frame_number = self.page_table[page_number]
        physical_address = (frame_number << self.page_size_bits) | offset
        return physical_address

    def get_page_table(self):
        return self.page_table

    def get_physical_memory(self):
        return self.physical_memory
