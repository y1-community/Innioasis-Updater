OUTPUT_FORMAT("elf32-littlearm", "elf32-bigarm", "elf32-littlearm")
OUTPUT_ARCH(arm)

ENTRY(start)

PHDRS
{
  text PT_LOAD FLAGS(5);
  data PT_LOAD FLAGS(6);
  bss PT_LOAD FLAGS(6);
}

SECTIONS
{
  . = 0x68000000;
  .text     : { *(.text.start) *(.text.main) *(.text   .text.*   .gnu.linkonce.t.*) } :text
  .rodata   : { *(.rodata .rodata.* .gnu.linkonce.r.*) } :text
  .data     : { *(.data   .data.*   .gnu.linkonce.d.*) } :data
  .bss      : { *(.bss    .bss.*    .gnu.linkonce.b.*) *(COMMON) } :bss
  /DISCARD/ : { *(.interp) *(.dynsym) *(.dynstr) *(.hash) *(.dynamic) *(.comment) }
}
