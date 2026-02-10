-- top 15 players
SELECT TOP 15 Player, Dependence_index
FROM player_stats
ORDER BY Dependence_index DESC;


--Duck rate vs dependence analysis
SELECT 
    Player,
    Duck,
    Dependence_index,
    Impact_score,
    CASE 
        WHEN Duck > (SELECT AVG(Duck) FROM player_stats) AND Dependence_index > (SELECT AVG(Dependence_index) FROM player_stats)
        THEN 'High Risk & High Dependence'
        ELSE 'Normal'
    END AS Risk_Category
FROM player_stats
ORDER BY Duck DESC, Dependence_index DESC;

-- top 15 layers impact score 

SELECT TOP 15 Player, Impact_score
FROM player_stats
ORDER BY Impact_score DESC;
  
