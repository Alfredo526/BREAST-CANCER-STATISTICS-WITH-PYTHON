import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import seaborn as sns


def age(dataset):
    # Print age statistics
    print('Here are some statistics:')
    print(f"Minimum age: {dataset['Age'].min()}")
    print(f"Maximum age: {dataset['Age'].max()}")
    print(f"Average age: {round(dataset['Age'].mean())}")
    print(f"Median age: {int(dataset['Age'].median())}")
    print(f"Most recurring age: {dataset['Age'].mode()[0]}")

    # Prepare data for plotting
    age_data = dataset.dropna(subset=['Age'])['Age']
    age_mean = age_data.mean()
    age_std = age_data.std()
    age_range = np.arange(age_mean - 3 * age_std, age_mean + 3 * age_std, 0.1)

    # Plot the age distribution using seaborn
    sns.histplot(age_data, kde=True, stat="density", bins=20)
    plt.plot(age_range, norm.pdf(age_range, age_mean, age_std))
    plt.xlabel('Age')
    plt.ylabel('Density')
    plt.title('Distribution of Age in Breast Cancer Patients')
    plt.show()


def gender(dataset):
    # Calculate the counts of each gender
    gender_counts = dataset['Gender'].value_counts()
    # Plot a pie chart using Matplotlib
    fig, ax = plt.subplots()
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90,
           counterclock=False)
    ax.set_title('Gender Distribution')
    plt.show()


def tumour_stage(dataset):
    # Group the data by Tumour_stage
    tumor_counts = dataset['Tumour_Stage'].value_counts()
    # Plot a pie chart using Matplotlib
    plt.pie(tumor_counts, labels=tumor_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Breast Cancer Tumour Stages')
    plt.show()


def tumour_stage_by_age(dataset):
    # Define the age groups
    age_groups = pd.cut(dataset['Age'], bins=[0, 40, 60, float('inf')], labels=['<40', '40-60', '60+'])

    # Group the data by cancer type and age groups
    grouped_data = dataset.groupby(['Tumour_Stage', age_groups]).size().unstack()

    # Plot the stacked bar chart
    grouped_data.plot(kind='bar', stacked=True)

    # Set the plot title and labels
    plt.title('Correlation between Cancer Type and Age Groups')
    plt.xlabel('Cancer Type')
    plt.ylabel('Count')

    # Show the legend
    plt.legend()

    # Show the plot
    plt.show()


def histology(dataset):
    print("Histology or Histologic Grade is a description of a tumor based on how abnormal the cancer cells and "
          "tissue look under a "
          "microscope and how quickly the cancer cells are likely to grow and spread. "
          "Low-grade cancer cells look more like normal cells and tend to grow and spread "
          "more slowly than high-grade cancer cells. Grading systems are different for each type of cancer. "
          "They are used to help plan treatment and determine prognosis. Also called grade and tumor grade.")
    # Get the count of each histology category
    histology_counts = dataset['Histology'].value_counts()
    # Create a pie chart of the histology categories
    fig, ax = plt.subplots()
    ax.pie(histology_counts, labels=histology_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title('Breast Cancer Histology')
    plt.show()


def histology_by_age(dataset):
    # Filter the data to only include alive and dead patients
    data = dataset[dataset['Patient_Status'].isin(['Alive', 'Dead'])]

    # Create a box plot to visualize the correlation between age and histology
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Histology', y='Age', data=dataset)

    # Set the plot title and labels
    plt.title('Correlation between Age and Histology')
    plt.xlabel('Histology')
    plt.ylabel('Age')

    # Show the plot
    plt.show()


def histology_by_tumour_stage(dataset):
    # Filter the data to only include alive and dead patients
    data = dataset[dataset['Patient_Status'].isin(['Alive', 'Dead'])]

    # Group the data by tumor stage and histology, and count the occurrences
    grouped_data = data.groupby(['Tumour_Stage', 'Histology']).size().unstack()

    # Plot a stacked bar plot to visualize the correlation between tumor stage and histology
    grouped_data.plot(kind='bar', stacked=True, figsize=(10, 6))

    # Set the plot title and labels
    plt.title('Correlation between Tumour Stage and Histology')
    plt.xlabel('Tumour Stage')
    plt.ylabel('Count')

    # Show the plot
    plt.show()


def ER_PR_status(dataset):
    # Create a dictionary to map the codes to the text labels
    code_to_label = {'Positive': 'Positive', 'Negative': 'Negative', 'Unknown': 'Unknown'}
    # Create a list of columns to plot
    columns_to_plot = ['ER status', 'PR status']
    # Plot the pie charts
    fig, axs = plt.subplots(1, len(columns_to_plot), figsize=(8, 4))
    for i, col in enumerate(columns_to_plot):
        # Group the data by column and count the values
        counts = dataset[col].value_counts()
        # Map the codes to the text labels
        labels = counts.index.map(code_to_label).tolist()
        # Plot the pie chart
        axs[i].pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False)
        axs[i].set_title(col.upper())
    # Adjust the layout
    plt.tight_layout()
    # Show the plot
    print('According to breastcancer.org people diagnosed with breast cancer that was '
          'estrogen-receptor-positive and progesterone-receptor-positive had a 30% '
          'to 60% lower risk of dying from breast cancer compared to people diagnosed '
          'with breast cancer that was positive for only one hormone receptor.')
    plt.show()


def HER2_status(dataset):
    # Get the count of positive and negative HER2 status
    her2_counts = dataset['HER2 status'].value_counts()
    # Create a pie chart using Matplotlib
    fig, ax = plt.subplots()
    ax.pie(her2_counts, labels=her2_counts.index, autopct='%1.1f%%', startangle=90, counterclock=False,
           colors=['green', 'red'])
    ax.set_title('HER2 Status')
    print(
        'According to the American Cancer Society, all breast cells have and are tested for an excess of human '
        'epidermal growth factor receptor 2, commonly referred to as HER2. '
        'HER2 proteins are receptors that control how the cells grow and divide. '
        'When breast tissue have extra HER2 receptors (overexpression), '
        'breast cells can multiply too quickly. Breast cancer cells with higher than normal levels of '
        'HER2 are called HER2-positive. These cancers tend to grow and spread faster than breast '
        'cancers that are HER2-negative, but are much more likely to respond to treatment with '
        'drugs that target the HER2 protein.')
    plt.show()


def HER2_status_by_age(dataset):
    # Filter the data to only include alive and dead patients
    data = dataset[dataset['Patient_Status'].isin(['Alive', 'Dead'])]

    # Create a box plot to visualize the correlation between age and HER2 status
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='HER2 status', y='Age', data=data)

    # Set the plot title and labels
    plt.title('Correlation between Age and HER2 Status')
    plt.xlabel('HER2 Status')
    plt.ylabel('Age')

    # Show the plot
    plt.show()


def surgery_type(dataset):
    # Get the count of each histology category
    surgery_type_counts = dataset['Surgery_type'].value_counts()
    # Create a pie chart of the histology categories
    fig, ax = plt.subplots()
    ax.pie(surgery_type_counts, labels=surgery_type_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title('Breast Cancer Surgery Types')
    plt.show()


def surgery_type_by_age(dataset):
    # Filter the data to only include alive and dead patients
    data = dataset[dataset['Patient_Status'].isin(['Alive', 'Dead'])]

    # Create a box plot to visualize the correlation between age and surgery type
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Surgery_type', y='Age', data=data)

    # Set the plot title and labels
    plt.title('Correlation between Age and Surgery Type')
    plt.xlabel('Surgery Type')
    plt.ylabel('Age')

    # Show the plot
    plt.show()


def surgery_by_tumour_stage(dataset):
    # Filter the data to only include alive and dead patients
    data = dataset[dataset['Patient_Status'].isin(['Alive', 'Dead'])]

    # Group the data by tumor stage and surgery type, and count the occurrences
    grouped_data = data.groupby(['Tumour_Stage', 'Surgery_type']).size().unstack()

    # Plot a stacked bar plot to visualize the correlation between tumor stage and surgery type
    grouped_data.plot(kind='bar', stacked=True, figsize=(10, 6))

    # Set the plot title and labels
    plt.title('Correlation between Tumor Stage and Surgery Type')
    plt.xlabel('Tumour Stage')
    plt.ylabel('Count')

    # Show the plot
    plt.show()


def surgery_by_histology_type(dataset):
    # Filter the data to only include alive and dead patients
    data = dataset[dataset['Patient_Status'].isin(['Alive', 'Dead'])]

    # Group the data by surgery type and histology, and count the occurrences
    grouped_data = data.groupby(['Surgery_type', 'Histology']).size().unstack()

    # Plot a stacked bar plot to visualize the correlation between surgery type and histology
    grouped_data.plot(kind='bar', stacked=True, figsize=(10, 6))

    # Set the plot title and labels
    plt.title('Correlation between Surgery Type and Histology')
    plt.xlabel('Surgery Type')
    plt.ylabel('Count')

    # Show the plot
    plt.show()


def patients_status(dataset):
    survival_counts = dataset['Patient_Status'].value_counts()
    plt.pie(survival_counts, labels=survival_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title("Breast Cancer Patients' Survival Status")
    plt.show()


def survival_by_tumour_stage(dataset):
    dataset['Tumour_Stage'] = dataset['Tumour_Stage'].replace(['I', 'II', 'III'], [1, 2, 3])
    dataset['Tumour_Stage'] = dataset['Tumour_Stage'].astype(int)

    # Create bins for tumor stages
    bins = [0, 1, 2, 3]

    # Create labels for tumor stages
    labels = ['Stage 1', 'Stage 2', 'Stage 3']

    # Cut the data into tumor stages
    dataset['tumour_stage'] = pd.cut(dataset['Tumour_Stage'], bins=bins, labels=labels)

    # Group the data by tumor stage and survival status
    tumour_stage_counts = dataset.groupby(['tumour_stage', 'Patient_Status']).size().unstack()

    # Plot a pie chart for each tumor stage using Matplotlib
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    fig.suptitle('Breast Cancer Survival by Tumour Stage')

    for i, stage in enumerate(labels):
        # Select the data for the current tumor stage
        stage_data = tumour_stage_counts.loc[stage]

        # Calculate the percentages of alive and dead patients
        alive_percent = stage_data['Alive'] / stage_data.sum() * 100
        dead_percent = stage_data['Dead'] / stage_data.sum() * 100

        # Create the pie chart for the current tumor stage
        axs[i].pie([alive_percent, dead_percent], labels=['Alive', 'Dead'], autopct='%1.1f%%')
        axs[i].set_title(stage)

    plt.show()


def survival_by_age_group(dataset):
    # Create bins for age groups
    bins = [20, 30, 40, 50, 60, 70, 80, 90]

    # Create labels for age groups
    labels = ['20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-90']

    # Cut the data into age groups
    dataset['age_group'] = pd.cut(dataset['Age'], bins=bins, labels=labels)

    # Group the data by age group and survival status
    age_group_counts = dataset.groupby(['age_group', 'Patient_Status']).size().unstack()

    # Plot a pie chart for each age group using Matplotlib
    fig, axs = plt.subplots(1, len(labels), figsize=(20, 5))

    for i, age_group in enumerate(labels):
        # Select the data for the current age group
        group_data = age_group_counts.loc[age_group]

        # Calculate the percentages of alive and dead patients
        alive_percent = group_data['Alive'] / group_data.sum() * 100
        dead_percent = group_data['Dead'] / group_data.sum() * 100

        # Create the pie chart for the current age group
        axs[i].pie([alive_percent, dead_percent], labels=['Alive', 'Dead'], autopct='%1.1f%%')
        axs[i].set_title(age_group)

    plt.suptitle("Survival Status by Age Group")
    plt.show()


def survival_by_histology(dataset):
    histology_counts = dataset.groupby(['Histology', 'Patient_Status']).size().unstack()

    # Create a pie chart for each histology using Matplotlib
    fig, axs = plt.subplots(1, len(histology_counts), figsize=(12, 4))

    for i, histology in enumerate(histology_counts.index):
        # Select the data for the current histology
        histology_data = histology_counts.loc[histology]

        # Calculate the percentages of alive and dead patients
        alive_percent = histology_data['Alive'] / histology_data.sum() * 100
        dead_percent = histology_data['Dead'] / histology_data.sum() * 100

        # Create the pie chart for the current histology
        axs[i].pie([alive_percent, dead_percent], labels=['Alive', 'Dead'], autopct='%1.1f%%')
        axs[i].set_title(histology)

    plt.suptitle('Survival by Histology')
    plt.show()


def survival_by_HER2_status(dataset):
    # Group the data by HER2 status and survival status
    her2_counts = dataset.groupby(['HER2 status', 'Patient_Status']).size().unstack()

    # Calculate the percentages of alive and dead patients for HER2 positive and negative
    her2_pos_alive_percent = her2_counts.loc['Positive']['Alive'] / her2_counts.loc['Positive'].sum() * 100
    her2_pos_dead_percent = her2_counts.loc['Positive']['Dead'] / her2_counts.loc['Positive'].sum() * 100
    her2_neg_alive_percent = her2_counts.loc['Negative']['Alive'] / her2_counts.loc['Negative'].sum() * 100
    her2_neg_dead_percent = her2_counts.loc['Negative']['Dead'] / her2_counts.loc['Negative'].sum() * 100

    # Plot the pie charts for HER2 positive and negative
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    plt.suptitle('Survival by HER2 Status')

    # HER2 positive
    axs[0].pie([her2_pos_alive_percent, her2_pos_dead_percent], labels=['Alive', 'Dead'], autopct='%1.1f%%')
    axs[0].set_title('HER2 Positive')

    # HER2 negative
    axs[1].pie([her2_neg_alive_percent, her2_neg_dead_percent], labels=['Alive', 'Dead'], autopct='%1.1f%%')
    axs[1].set_title('HER2 Negative')

    plt.show()


def survival_by_surgery_type(dataset):
    # Group the data by surgery type and survival status
    surgery_counts = dataset.groupby(['Surgery_type', 'Patient_Status']).size().unstack()

    # Plot a pie chart for each surgery type using Matplotlib
    fig, axs = plt.subplots(1, len(surgery_counts), figsize=(10, 4))

    for i, surgery_type in enumerate(surgery_counts.index):
        # Select the data for the current surgery type
        surgery_data = surgery_counts.loc[surgery_type]

        # Calculate the percentages of alive and dead patients
        alive_percent = surgery_data['Alive'] / surgery_data.sum() * 100
        dead_percent = surgery_data['Dead'] / surgery_data.sum() * 100

        # Create the pie chart for the current surgery type
        axs[i].pie([alive_percent, dead_percent], labels=['Alive', 'Dead'], autopct='%1.1f%%')
        axs[i].set_title(surgery_type)

    plt.suptitle("Survival Rate by Surgery Type", fontsize=16)
    plt.show()


def distribution_of_protein_values(dataset):
    # Filter the data to only include alive and dead patients
    data = dataset[dataset['Patient_Status'].isin(['Alive', 'Dead'])]

    # Create distribution plot for each protein
    fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(15, 5))

    for i, protein in enumerate(['Protein1', 'Protein2', 'Protein3', 'Protein4']):
        sns.histplot(data=data, x=protein, hue='Patient_Status', ax=axs[i], alpha=0.5)
        axs[i].set_title(protein)

    # Add overall title
    plt.suptitle('Distribution of Protein Levels by Patient Status')

    # Show the plots
    plt.show()
