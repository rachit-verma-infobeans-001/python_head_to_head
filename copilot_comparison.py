import pandas as pd

def head_to_head_comparison(team1, team2, match_data):
    """
    Compare two cricket teams head-to-head based on matches they played against each other.

    Args:
        team1 (str): Name of the first team.
        team2 (str): Name of the second team.
        match_data (pd.DataFrame): DataFrame containing match data with columns:
                                   ['team1', 'team2', 'winner'].

    Returns:
        dict: A dictionary with head-to-head statistics.
    """
    # Filter matches where the two teams played against each other
    head_to_head_matches = match_data[
        ((match_data['team1'] == team1) & (match_data['team2'] == team2)) |
        ((match_data['team1'] == team2) & (match_data['team2'] == team1))
    ]

    # Calculate wins for each team
    team1_wins = (head_to_head_matches['winner'] == team1).sum()
    team2_wins = (head_to_head_matches['winner'] == team2).sum()
    draws = (head_to_head_matches['winner'] == 'Draw').sum()

    # Return the results
    return {
      'team1': team1,
      'team2': team2,
      'team1_wins': team1_wins,
      'team2_wins': team2_wins,
      'draws': draws,
      'total_matches': len(head_to_head_matches)
    }

# Example usage
if __name__ == "__main__":
  # Sample match data
  data = {
      'team1': ['India', 'Australia', 'India', 'India', 'Australia'],
      'team2': ['Australia', 'India', 'Australia', 'England', 'India'],
      'winner': ['India', 'Australia', 'India', 'India', 'Draw']
  }
  match_data = pd.DataFrame(data)

  # Perform head-to-head comparison
  result = head_to_head_comparison('India', 'Australia', match_data)
  print(result)
