// https://app.codesignal.com/challenge/uFMZ9Wm3MK3f7j5uG
// Solution by breathermachine
// bool bishopAndPawn(char * bishop, char * pawn) { }
#define bishopAndPawn(B, P) abs(*P++ - *B++) == abs(*P - *B)