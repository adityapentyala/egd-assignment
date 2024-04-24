library("dplyr")
library("readxl")
library("tidyr")

regression_data <- as.data.frame(read_excel("data/regression_df_dummy_ratios.xlsx"))

names(regression_data) <- c("idx", "lnPCGDP", "grossDomSavings", "totalLaborForce", "NetTradePercent", 
    "CPI", "FDIPercent", "developingDummy", "underdevelopedDummy", "GDPGrowthRate")

interaction_model <- lm(GDPGrowthRate ~ lnPCGDP + grossDomSavings + totalLaborForce + NetTradePercent + CPI + 
    developingDummy + underdevelopedDummy + lnPCGDP:totalLaborForce + lnPCGDP:developingDummy + lnPCGDP:underdevelopedDummy +
    grossDomSavings:developingDummy + grossDomSavings:underdevelopedDummy + totalLaborForce:developingDummy +
    totalLaborForce:underdevelopedDummy + CPI:developingDummy + CPI:underdevelopedDummy + FDIPercent:developingDummy +
    FDIPercent:underdevelopedDummy, data=regression_data)