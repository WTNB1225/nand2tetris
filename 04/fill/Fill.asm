(LOOP)
    @24576 // 押されているキーの ASCII コードが現れる場所
    // 何も押されていない場合は 0 が現れる
    D = M // D = Memory[24576]
    @WHITE // キーが押されている場合は (WHITE) に移動
    D;JGT // if D > 0, jump to WHITE
(BLACK)
    @i
    M = 0 // Memory[i] = 0
(BLACKLOOP)
    @i
    D = M // D = Memory[i]
    @8191
    D = D - A // D = D - 8191
    @BLACKEND
    D;JGT // if D > 0, jump to END
    @i
    D = M // D = Memory[i]
    @SCREEN
    A = A + D // D = SCREEN + Memory[i]
    M = -1 // paint to black
    @i
    M = M + 1 // Memory[i] += 1
    @BLACKLOOP
    0;JMP
(BLACKEND)
    @LOOP
    0;JMP // 無限ループ
(WHITE)
    @j
    M = 0
(WHITELOOP)
    @j
    D = M // D = Memory[j]
    @8191
    D = D - A // D = D - 8191
    @WHITEEND
    D;JGT // if D > 0, jump to END
    @j
    D = M // D = Memory[j]
    @SCREEN
    A = A + D // A = SCREEN + Memory[j]
    M = 0 // paint to white
    @j
    M = M + 1 // j = j + 1
    @WHITELOOP
    0;JMP
(WHITEEND)
    @LOOP
    0;JMP