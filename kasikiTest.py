'''
Tyler Carpenter
CIS 3362 Guha

This is a program that performs the Kasiki Test
The Kasiski Test is finding the lengths between pairs of repetitions of the ciphertext, and
then taking the greatest common divisor of each of these values, since the keyword length is likely
to divide into each of these values. Thus, list out each starting index of a repeated n-gram in sorted
order, and for each successive pair of items on the list, take their gcd. Then, take the gcd of all of
these values and that gives you the most likely keyword length.


Change the length and the ciphertext to use.
'''


#identifies sequences of characters within the ciphertext that appear more than once
def find_repeated_sequences(ciphertext, length):
    
    sequences = {}
    for i in range(len(ciphertext) - length + 1):
        seq = ciphertext[i:i + length]
        if seq in sequences:
            sequences[seq].append(i)
        else:
            sequences[seq] = [i]
    
    #return sequences with more than one occurrence
    repeated_sequences = {seq: positions for seq, positions in sequences.items() if len(positions) > 1}
    print(f"Repeated sequences: {repeated_sequences}")  # Debugging line
    return repeated_sequences


#ccomputes the differences between the positions of repeated sequences within the ciphertext
def calculate_distances(positions):
    
    distances = []
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            distances.append(positions[j] - positions[i])
    return distances

def gcd(a, b):
    
    while b:
        a, b = b, a % b
    return a

#identifies all divisors of the greatest common divisor (GCD) of a list of distances
def find_common_divisors(distances):
    
    common_divisors = set()
    if not distances:
        return common_divisors
    #compute GCD of all distances
    current_gcd = distances[0]
    for distance in distances[1:]:
        current_gcd = gcd(current_gcd, distance)
    
    #find all divisors of the GCD
    for i in range(1, int(current_gcd**0.5) + 1):
        if current_gcd % i == 0:
            common_divisors.add(i)
            common_divisors.add(current_gcd // i)
    return common_divisors

#enter ciphertext here
#ciphertext = "wywormwhzkejpvhrrumydrrredjouvbpqtywjhejpsqysygewornuqssgfbpuexwkcdghowysjmxowfcbyvkzrmbpswppcbdmmhsiprlsvkwicmglczwrpodjhlsxswfbwbmpivfalxpofcnesdrkvarlsuuthmsbvgsygjsfrzhwjsqufkmqdkisaraywncjceblkwoyjsuvstrisqxieqloufdalxrhuckparhisermcderhgjdlkilsrnhibayxrlkmksasoctelhdkvbkripufaicfbleuerxypvojbkowksjbsvorfo"
ciphertext= "phbwzexssywsmulqwewbjaghktiwofpcaeeoiecphabqjaqpabjerflfmhwyhmtovksfkbnkysiuxjchdaoikagwwzxaepktiholpomlvrsffgdfesfdasseatairpqtbvotkekuzpcsbivizejzfpkmiykqvdqvanviiukshnyrhwjrvzagdamswrmnsgdekizeemiyhemmenslfqwdoiifmdwacmtrpopfpfwcmmmuxtsfwnwnfnwwcbgbxlzzhevrdavolojacfpekxfsiehualtwkzsessnofqvfsnznemmlvxedhcnisiwavsczawhvbfazubkdeytw"
#enter sequence length here
length = 3

#analyze ciphertext
sequences = find_repeated_sequences(ciphertext, length)
all_distances = []
for positions in sequences.values():
    distances = calculate_distances(positions)
    all_distances.extend(distances)

