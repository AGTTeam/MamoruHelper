.nds

.open "data/repack/arm9.bin",0x02000000
;Using free space from 0x020E5614 to 0x020E5907 for custom code
;Fix the game to run on no$gba
;More info: https://github.com/Arisotura/melonDS/issues/559
.org 0x020e5614
.area 0x1B0
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
  ;Check what font we're using and add 0x5f for LC10
  ldr r2,[r13,0x2c]
  cmp r2,0x8
  addne r0,r0,0x5f
  ;Set r0 to the character spacing
  ldrb r0,[r0]
  strb r0,[r13,0x28]
  ;Restore cmp register
  mov r0,0x0
  cmp r0,0x0
  b NAMEPLATE_VWF_RETURN
  .pool

;Center the enemy nameplates when using ASCII
NAMEPLATE_CENTER:
  push {r0}
  ;The current character is in r5, and r5 is used for the width
  ldr r0,=FONT_LC08
  add r0,r0,r5
  sub r0,r0,0x20
  ;Check what font we're using and add 0x5f for LC10
  ldr r5,[r13,0x2c]
  cmp r5,0x8
  addne r0,r0,0x5f
  ;Set the width
  ldrb r5,[r0]
  pop {r0}
  b NAMEPLATE_CENTER_RETURN
  .pool

;Set the default keybaord as Alphabet
DEFAULT_KEYBOARD:
  mov r2,0x2
  str r2,[r10,0x3e0]
  mov r2,0x0
  b DEFAULT_KEYBOARD_RETURN

;Fit "Permanent Skill" in menu header
PERMANENT_SKILL:
  ldrb r2,[r7,0x4]
  cmp r2,0x50
  mov r2,0x20
  addeq r2,r2,0x04
  b PERMANENT_SKILL_RETURN

;Move the 2nd item description line down if there's a line break in the first one
;r7 = number of the line
;r10 = line spacing, default is 0x0c
;r12 = pointer to the string
ITEM_DESCR:
  cmp r7,0x00
  bne ITEM_DESCR_END
  mov r10,0x0c
  mov r1,0x0
  ITEM_DESCR_LOOP:
  ldrb r2,[r12,r1]
  cmp r2,0x0a
  beq ITEM_DESCR_LB
  cmp r2,0x0
  beq ITEM_DESCR_END
  add r1,r1,0x1
  b ITEM_DESCR_LOOP
  ITEM_DESCR_LB:
  mov r10,0x14
  ITEM_DESCR_END:
  mov r1,r4
  b ITEM_DESCR_RETURN

;Import the font data
FONT_LC08:
  .import "data/font_data.bin"
.endarea

;Fix "Liruka Village" not being centered
.org 0x020f7268
  ;Original: .sjis "　　　　　　%s"
  .sjis "　　　　 %s　"

;Extend "Permanent Skill" menu header
.org 0x2085438
  ;Original: mov r1,0x8
  mov r1,0x0c
;Move the text a little to the right
.org 0x020858b4
  ;Original: mov r2,0x20
  b PERMANENT_SKILL
  PERMANENT_SKILL_RETURN:

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
.org 0x020a51fc
  ;Original: str r2,[r10,0x3e0]
  b DEFAULT_KEYBOARD
  DEFAULT_KEYBOARD_RETURN:
.org 0x020784d8
  ;Original: mov r1,r4
  b ITEM_DESCR
  ITEM_DESCR_RETURN:

.close
