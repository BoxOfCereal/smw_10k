import csv

def convert_file_paths_to_links(csv_file_path, output_file_path, base_url):
    with open(csv_file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        fieldnames = reader.fieldnames
        rows = []
        for row in reader:
            filename = row['filename']
            filename_parts = filename.split('\\')
            file_name = filename_parts[-1]
            link = base_url + file_name.replace(' ', '%20')
            row['filename'] = link
            rows.append(row)
    
    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(rows)

# Example usage
csv_file_path = 'smw_10k.csv'
output_file_path = 'C:\\Users\\SeltT\\OneDrive\\Desktop\\BizHawk-2.9-win-x64\\data\\smw-small\\smw_10k_fix.csv'
base_url = 'https://raw.githubusercontent.com/BoxOfCereal/smw_10k/main/smw_10k/'

convert_file_paths_to_links(csv_file_path, output_file_path, base_url)
print("Conversion complete. Output saved to", output_file_path)
