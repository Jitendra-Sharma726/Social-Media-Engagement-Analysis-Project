import pandas as pd
import matplotlib
matplotlib.use("Agg")  # headless mode

import matplotlib.pyplot as plt

import seaborn as sns

# Apply seaborn styling
sns.set_theme(style="whitegrid")

# 1. Load Data
def load_data():
    """
    Create and return a DataFrame containing social media engagement data.
    """
    data = {
        "post_id": [1, 2, 3, 4, 5, 6, 7, 8],
        "likes": [120, 340, 560, 230, 410, 290, 600, 150],
        "comments": [30, 80, 120, 45, 95, 60, 150, 20],
        "shares": [15, 40, 75, 25, 60, 35, 100, 10]
    }
    
    df = pd.DataFrame(data)
    print("Data loaded successfully!")
    return df

# 2. Compute Engagement
def analyze_engagement(df):
    """
    Calculate total engagement column.
    """
    df["total_engagement"] = df["likes"] + df["comments"] + df["shares"]
    print("\nEngagement Summary (First 5 rows):")
    if "total_engagement" in df.columns:
        print(df[["post_id", "total_engagement"]].head())
    return df

# 3. Stacked Bar Chart (Matplotlib)
def plot_engagement_composition(df):
    """
    Visualize Likes, Comments, and Shares using a Stacked Bar Chart.
    """
    plt.figure(figsize=(10, 6))

    # Layer 1: Likes (Base)
    plt.bar(df["post_id"], df["likes"], label="Likes", color="#3498db")
    
    # Layer 2: Comments (Stacked on Likes)
    plt.bar(df["post_id"], df["comments"], bottom=df["likes"], label="Comments", color="#e67e22")
    
    # Layer 3: Shares (Stacked on Likes + Comments)
    # We calculate the combined bottom height
    bottom_heights = df["likes"] + df["comments"]
    plt.bar(df["post_id"], df["shares"], bottom=bottom_heights, label="Shares", color="#2ecc71")

    plt.title("Engagement Composition per Post (Stacked)")
    plt.xlabel("Post ID")
    plt.ylabel("Count")
    plt.legend()
    
    filename = "engagement_composition.png"
    plt.savefig(filename)
    print(f"Chart saved: {filename}")

# 4. Bubble Chart (Seaborn)
def plot_metrics_relationship(df):
    """
    Visualize Likes vs Comments, with bubble size representing Shares.
    """
    plt.figure(figsize=(8, 6))

    sns.scatterplot(
        data=df,
        x="likes",
        y="comments",
        size="shares"      # 3rd Variable: Size
    )

    plt.title("Likes vs Comments (Size = Shares)")
    plt.xlabel("Likes")
    plt.ylabel("Comments")
    
    filename = "metrics_relationship.png"
    plt.savefig(filename)
    print(f"Chart saved: {filename}")

# 5. Box Plot with Melt
def plot_engagement_distribution(df):
    """
    Compare distributions of Likes vs Comments vs Shares.
    """
    # Step 1: Reshape data from Wide to Long format
    melted_df = df.melt(
        id_vars="post_id", 
        value_vars=["likes", "comments", "shares"], 
        var_name="metric", 
        value_name="count"
    )

    plt.figure(figsize=(8, 6))

    sns.boxplot(
        data=melted_df,
        x="metric",
        y="count",
        palette="Set2",
        hue="metric", # Added to avoid warnings
        legend=False
    )

    plt.title("Distribution of Engagement Metrics")
    plt.xlabel("Metric Type")
    plt.ylabel("Count")

    filename = "engagement_distribution.png"
    plt.savefig(filename)
    print(f"Chart saved: {filename}")

if __name__ == "__main__":
    print("Social Media Engagement Analyzer Project\n")

    df = load_data()
    
    if df is not None:
        df = analyze_engagement(df)

        if "total_engagement" in df.columns:
            plot_engagement_composition(df)
            plot_metrics_relationship(df)
            plot_engagement_distribution(df)
        else:
            print("... Please complete the analyze_engagement function.")
    else:
        print("... Please complete the load_data function.")


