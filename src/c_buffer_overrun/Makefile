all: main.exposed.elf main.stack-protector.elf main.stack-protector-all.elf main.stack-protector-strong.elf simple.exposed.elf

main.exposed.elf: main.c
	gcc -fno-stack-protector -o $@ $<
main.stack-protector.elf: main.c
	gcc -fstack-protector -o $@ $<
main.stack-protector-all.elf: main.c
	gcc -fstack-protector-all -o $@ $<
main.stack-protector-strong.elf: main.c
	gcc -fstack-protector-strong -o $@ $<
simple.exposed.elf: simple.c
	gcc -Wno-stringop-overflow -o $@ $<
