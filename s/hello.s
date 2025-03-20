	.file	"hello.c"
	.machinemode zarch
	.machine "arch14"
.text
	.section	.rodata.str1.2,"aMS",@progbits,1
	.align	2
.LC0:
	.string	"Hello world!"
	.section	.text.startup,"ax",@progbits
	.align	8
	.align	16
.globl main
	.type	main, @function
main:
.LFB23:
	.cfi_startproc
	stmg	%r14,%r15,112(%r15)
	larl	%r2,.LC0
	.cfi_offset 14, -48
	.cfi_offset 15, -40
	lay	%r15,-160(%r15)
	.cfi_def_cfa_offset 320
	brasl	%r14,puts@PLT
	lghi	%r2,0
	lmg	%r14,%r15,272(%r15)
	.cfi_restore 15
	.cfi_restore 14
	.cfi_def_cfa_offset 160
	br	%r14
	.cfi_endproc
.LFE23:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0"
	.section	.note.GNU-stack,"",@progbits
