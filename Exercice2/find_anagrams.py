from mrjob.job import MRJob

class AnagramFinder(MRJob):

    def mapper(self, _, line):
        """
        Mapper : trie les lettres de chaque mot pour produire une clé canonique.
        """
        for word in line.split(","):
            # Supprimer les espaces et convertir en minuscule
            clean_word = word.strip().lower()
            
            # Ignorer les mots vides
            if not clean_word:
                continue
            
            # Remplacer les voyelles accentuées
            clean_word = clean_word.replace("é", "e").replace("è", "e").replace("ê", "e")
            clean_word = clean_word.replace("à", "a").replace("â", "a").replace("î", "i").replace("ï", "i")
            clean_word = clean_word.replace("ô", "o").replace("û", "u").replace("ù", "u")

            # Trier les lettres pour produire une clé canonique
            sorted_letters = "".join(sorted(clean_word))
            yield sorted_letters, clean_word

    def reducer(self, key, words):
        """
        Reducer : regroupe les mots ayant la même clé et filtre les groupes de taille < 2.
        """
        anagram_list = list(words)
        if len(anagram_list) > 1:
            yield key, anagram_list

if __name__ == "__main__":
    AnagramFinder.run()
