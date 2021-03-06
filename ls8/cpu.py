"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010
PUSH = 0b01000101
POP = 0b01000110

SP = 7

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.memory = [0] * (256 * 8)
        self.register = [0] * 8
        self.PC = 0
        self.running = True
        self.branch_table = {
            HLT: self.op_HLT,
            LDI: self.op_LDI,
            PRN: self.op_PRN,
            MUL: self.op_MUL,
            PUSH: self.op_PUSH,
            POP: self.op_POP
        }

    def op_HLT(self, operand_a, operand_b):
        self.running = False

    def op_LDI(self, operand_a, operand_b):
        self.register[operand_a] = operand_b
        self.PC += 3

    def op_PRN(self, operand_a, operand_b):
        print(self.register[operand_a])
        self.PC += 2

    def op_MUL(self, operand_a, operand_b):
        self.alu('MUL', operand_a, operand_b)
        self.PC += 3

    def op_PUSH(self, operand_a, operand_b):
        self.push(self.register[operand_a])
        self.PC += 2

    def op_POP(self, operand_a, operand_b):
        self.register[operand_a] = self.pop()
        self.PC += 2

    def push(self, value):
        self.register[SP] -= 1
        self.ram_write(value, self.register[7])

    def pop(self):
        value = self.ram_read(self.register[7])
        self.register[SP] += 1
        return value

    def ram_read(self, address):
        return self.memory[address]

    def ram_write(self, value, address):
        self.memory[address] = value

    def load(self):
        """Load a program into memory."""
        address = 0
        with open(sys.argv[1]) as f:
            for line in f:
                comment_split = line.split("#")
                num = comment_split[0].strip()
                if num == '':
                    continue
                instruction = int(num, 2)

                self.memory[address] = instruction
                address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.register[reg_a] += self.register[reg_b]
        elif op == "MUL":
            self.register[reg_a] *= self.register[reg_b]
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
            print(" %02X" % self.register[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while self.running == True:
            IR = self.ram_read(self.PC)
            operand_a = self.ram_read(self.PC + 1)
            operand_b = self.ram_read(self.PC + 2)

            if int(bin(IR), 2) in self.branch_table:
                self.branch_table[IR](operand_a, operand_b)
            else:
                raise Exception(f"Invalid {int(bin(IR), 2)} not in branch table \t {list(self.branch_table.keys())}")
