from NursingProfileManager import NursingProfileManager
from data import moms, nurses


def main():
    profile_manager = NursingProfileManager(moms, nurses)
    mom_tasks = profile_manager.get_mom()
    nurse_tasks = profile_manager.get_nurse()
    similarity_embed = profile_manager.get_embeddings(mom_tasks, nurse_tasks)
    # print(similarity_embed)
    profile_manager.get_best_embed(similarity_embed)


if __name__ == "__main__":
    main()
