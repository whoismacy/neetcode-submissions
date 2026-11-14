class Solution {

    fun encode(strs: List<String>): String {
        var str = ""
        for (string in strs) {
            str += "${string.length}~$string"
        }
        return str
    }

    fun decode(str: String): List<String> {
        val words = mutableListOf<String>()
        var wordIndex = 0
        var lengthIndex: Int

        while (wordIndex < str.length) {
           lengthIndex = wordIndex 
           while (str[lengthIndex] != '~') {
                lengthIndex += 1
           }
           val wordLength = str.slice(wordIndex..<lengthIndex).toInt()
           val word = str.slice(lengthIndex+1..<lengthIndex+1+wordLength)
           words.add(word)
           wordIndex = wordLength + 1 + lengthIndex
        }

        return words
    }
}
