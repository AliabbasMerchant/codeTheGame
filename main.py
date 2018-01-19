import inning
import consolidate
import dream11

file_list = []
inn = inning.Inning()
for i in range(1,11) :
    inn.read_csv("outputf" + str(i) + "1st.csv")
    inn.allot_data()
    inn.calculate_scores()
    file_list.append(inn.save_to_json())
    if i == 1:
        inn.read_csv("outputf" + str(i) + "2nd.csv")
        inn.allot_data()
        inn.calculate_scores()
        file_list.append(inn.save_to_json())
    if i == 2:
        inn.read_csv("outputf" + str(i) + "2nd.csv")
        inn.allot_data()
        inn.calculate_scores()
        file_list.append(inn.save_to_json())
consolidate = consolidate.Consolidate()
consolidate.consolidate(file_list)
consolidate.save_to_json()

Dream11 = dream11.dream11()
Dream11.read()
Dream11.save_to_json()

print("DONE!!!")
