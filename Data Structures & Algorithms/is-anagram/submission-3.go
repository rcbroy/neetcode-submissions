func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    var schars [26]int
    var tchars [26]int
    for i := range s {
        schars[int(s[i])-'a']++
        tchars[int(t[i])-'a']++
    }
    return schars == tchars
}
