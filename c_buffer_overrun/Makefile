all: main.normal.elf main.without-protector.elf

main.normal.elf: main.c
	gcc -o $@ $< -fno-stack-protector
main.without-protector.elf: main.c
	gcc -o $@ $<
