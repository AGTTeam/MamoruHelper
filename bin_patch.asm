.nds

.open "data/repack/arm9.bin",0x02000000
;Fix the game to run on no$gba
;More info: https://github.com/Arisotura/melonDS/issues/559
.org 0x020108c0
  b MEMSET_HACK
  MEMSET_HACK_RETURN:
.org 0x020e5614
  MEMSET_HACK:
  ;Original jump
  bcc 0x0201094c
  ;Compare r2 to the bugged value
  ldr r1,=0x2d8bc0
  cmp r1,r2
  bne MEMSET_HACK_RETURN
  ;Set r2 to 0x0 in that case, then return to regular execution
  mov r2,0x00
  b MEMSET_HACK_RETURN
  .pool

;Fix "Liruka Village" not being centered
.org 0x020f7268
  ;Original: .sjis "　　　　　　%s"
  .sjis "　　　　　%s　"

.close
