Function commonCharacterCount(s1 As String, s2 As String) As Integer 
   Dim i, j As Integer
        Dim count = 0
top:
        For i = 0 To s1.Length - 1
            For j = 0 To s2.Length - 1
                If s1(i) = s2(j) Then
                    count += 1
                    s1 = s1.Remove(i, 1)
                    s2 = s2.Remove(j, 1)
                    GoTo top
                End If
            Next
        Next
        Return count
End Function