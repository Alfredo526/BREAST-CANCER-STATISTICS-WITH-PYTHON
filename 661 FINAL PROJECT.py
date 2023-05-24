import pandas as pd
import chart_generator


def breast_cancer_statistics_program(dataset):
    """
     Display breast cancer statistics and correlations based on user input.
     Prompts the user to choose an area of interest and displays charts and statistics based on the user's choice.
     Raises:
         NameError: If NameError: name 'breast_cancer_df' is not defined
     """

    print('Breast Cancer Statistics and Correlations Program\n')
    print("Close windows with charts to continue the Program.")
    print(
        "All charts were made possible with AI but it never got it right the first time. It took trial and error.\n")
    statistics_answer = input(
        'Do you want to know the statistics and correlations of a dataset of 335 people (y/n)?')
    if statistics_answer == 'y':
        while True:
            category = input('\nWhich of the following areas are you interested in learning about? '
                             'If none type none.\n'
                             '\nAge\nGender'
                             '\nTumour stage\nHistology\nER and PR status\nHER2 status\nSurgery type\nPatients '
                             'status\nDistribution of Protein values\n\n')
            if category == 'Age':
                chart_generator.age(dataset)
                chart_generator.survival_by_age_group(dataset)
            elif category == 'Gender':
                chart_generator.gender(dataset)
            elif category == 'Tumour stage':
                chart_generator.tumour_stage(dataset)
                chart_generator.tumour_stage_by_age(dataset)
                chart_generator.survival_by_tumour_stage(dataset)
            elif category == 'Histology':
                chart_generator.histology(dataset)
                chart_generator.histology_by_age(dataset)
                chart_generator.histology_by_tumour_stage(dataset)
                chart_generator.survival_by_histology(dataset)
            elif category == 'ER and PR status':
                chart_generator.ER_PR_status(dataset)
            elif category == 'HER2 status':
                chart_generator.HER2_status(dataset)
                chart_generator.HER2_status_by_age(dataset)
                chart_generator.survival_by_HER2_status(dataset)
            elif category == 'Surgery type':
                chart_generator.surgery_type(dataset)
                chart_generator.surgery_type_by_age(dataset)
                chart_generator.surgery_by_tumour_stage(dataset)
                chart_generator.surgery_by_histology_type(dataset)
                chart_generator.survival_by_surgery_type(dataset)
            elif category == 'Patients status':
                chart_generator.patients_status(dataset)
            elif category == 'Distribution of Protein values':
                chart_generator.distribution_of_protein_values(dataset)
            elif category == 'none':
                print('\nMy program does not have what you are looking for. Try another program.')
                break
            else:
                print('Please pick a category.')
                continue
            if input('\nDo you want to learn other areas (y/n)?') == 'y':
                continue
            else:
                print('\nMy program does not have what you are looking for. Try another program.')
                break
    else:
        print('\nMy program does not have what you are looking for. Try another program.')


if __name__ == "__main__":
    breast_cancer_df = pd.read_csv('breast_cancer_survival.csv')
    try:
        breast_cancer_statistics_program(breast_cancer_df)
        while input('\nTry the program again (y/n)?') == 'y':
            breast_cancer_statistics_program(breast_cancer_df)
        print('Thanks for using my program.')
    except Exception as e:
        print(f'An error occurred: {e}')
