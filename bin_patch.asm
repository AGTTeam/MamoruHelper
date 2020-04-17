.nds

.open "data/repack/arm9.bin",0x02000000
;Fix the game to run on no$gba
;More info: https://github.com/Arisotura/melonDS/issues/559
.org 0x020e5614
  MEMSET_HACK:
  ;Original jump
  bcc 0x0201094c
  ;Compare r2 to the bugged value
  ldr r1,=0x2d8bc0
  cmp r1,r2
  bne MEMSET_HACK_RETURN
  ;Set r2 to 0 in that case, then return to regular execution
  mov r2,0x0
  b MEMSET_HACK_RETURN
  .pool

;VWF for the enemy nameplates
NAMEPLATE_VWF:
  ;r0 is 0 if the character in r9 is ascii
  cmp r0,0x0
  bne NAMEPLATE_VWF_RETURN
  ;Get the character width and set r13+0x28
  ldr r0,=FONT_LC08
  add r0,r0,r9
  sub r0,r0,0x20
  ldrb r0,[r0]
  strb r0,[r13,0x28]
  b NAMEPLATE_VWF_RETURN
  .pool

;Center the enemy nameplates when using ASCII
NAMEPLATE_CENTER:
  ;The current character is in r5, and r5 is used for the width
  ldr r0,=FONT_LC08
  add r0,r0,r5
  sub r0,r0,0x20
  ldrb r5,[r0]
  mov r0,0x0
  b NAMEPLATE_CENTER_RETURN
  .pool

;Import the font data
FONT_LC08:
  .import "data/font_data.bin"

;Fix "Liruka Village" not being centered
.org 0x020f7268
  ;Original: .sjis "　　　　　　%s"
  .sjis "　　　　 %s　"

;Inject custom code
.org 0x020108c0
  b MEMSET_HACK
  MEMSET_HACK_RETURN:
.org 0x0208da24
  ;Original: ldr r5,[r13,0x28]
  b NAMEPLATE_CENTER
  NAMEPLATE_CENTER_RETURN:
.org 0x0208dbf0
  ;Original: cmp r0,0x0
  b NAMEPLATE_VWF
  NAMEPLATE_VWF_RETURN:

.close
