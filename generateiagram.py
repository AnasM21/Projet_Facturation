import matplotlib.pyplot as plt

# Create a figure for the MCD (Modèle Conceptuel de Données) with bigger rectangles
fig, ax = plt.subplots(figsize=(10, 7))

# Define entities and their attributes
entities = {
    "Client": ["ID_Client (PK)", "Nom", "Email", "Adresse"],
    "Check (Chèque)": ["ID_Check (PK)", "Numéro de Chèque", "Montant", "Statut", "Date d'Émission", "ID_Client (FK)"],
    "Invoice (Facture)": ["ID_Invoice (PK)", "Numéro de Facture", "Montant", "Statut", "Date d'Émission", "Date d'Échéance", "ID_Client (FK)"]
}

# Draw rectangles and text for each entity with larger sizes
positions = {
    "Client": (1, 5),
    "Check (Chèque)": (5, 8),
    "Invoice (Facture)": (5, 2)
}

# Increase rectangle size for better visibility
rect_width = 4
rect_height = 2.5

for entity, (x, y) in positions.items():
    # Draw rectangle for the entity
    ax.add_patch(plt.Rectangle((x, y), rect_width, rect_height, fill=None, edgecolor='black', linewidth=1.5))
    # Add the entity name
    plt.text(x + 0.1, y + rect_height - 0.3, entity, fontsize=12, weight='bold')
    # Add the attributes
    for i, attribute in enumerate(entities[entity]):
        plt.text(x + 0.1, y + rect_height - 0.9 - i * 0.6, attribute, fontsize=10)

# Draw relationships
plt.arrow(5, 6.25, 0.5, 1.5, head_width=0.2, head_length=0.3, fc='black', ec='black')  # Client to Check
plt.arrow(5, 5.25, 0.5, -1.5, head_width=0.2, head_length=0.3, fc='black', ec='black')  # Client to Invoice

# Add relationship labels
plt.text(5.2, 7.8, "1,N", fontsize=12)
plt.text(5.2, 3.8, "1,N", fontsize=12)

# Set axis limits and hide axes
plt.xlim(0, 12)
plt.ylim(0, 12)
plt.axis('off')

# Save the figure with bigger rectangles
plt.savefig("./MCD_Projet_Facturation_Bigger_Entities.png", bbox_inches='tight')
plt.show()
