"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        memory = [0] * (256 * 8)
        register = [0] * 8
        PC = []

    def ram_read(self, address):
        return self.memory[address]

    def ram_write(self, value, address):
        self.memory[address] = value

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        run = True

        while run == True:
            IR = ram_read(self.PC)

            opcode = IR[:1]

            if opcode == 00:
                self.PC += 1
            elif opcode == 1:
                operand_a = ram_read(self.PC + 1)
                self.PC += 2
            elif opcode == 10:
                operand_a = ram_read(self.PC + 1)
                operand_b = ram_read(self.PC + 2)
                self.PC += 3

            if IR == HLT:
                run = False
            elif IR == LDI:
                self.register[operand_b] = operand_a
            elif IR == PRN:
                print(self.register[operand_a])
