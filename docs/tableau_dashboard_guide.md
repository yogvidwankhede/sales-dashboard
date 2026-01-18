# Tableau Dashboard Building Guide
## Sales Intelligence Dashboard

---

## Dashboard 1: Executive Summary

### Objective
High-level overview showing current revenue, KPIs, and the $1.5M opportunity breakdown

### Layout Structure
```
┌─────────────────────────────────────────────────────────┐
│  SALES INTELLIGENCE DASHBOARD - EXECUTIVE SUMMARY       │
├─────────────────┬─────────────────┬─────────────────────┤
│  Total Revenue  │  Profit Margin  │  Active Customers   │
│  $753.7M       │     54.7%       │     8,974           │
├─────────────────┴─────────────────┴─────────────────────┤
│          Revenue Opportunity Breakdown ($1.5M)          │
│  [Horizontal Bar Chart showing 4 opportunities]         │
├──────────────────────────────────────────────────────────┤
│  Revenue Trend (Line Chart)         │  Segment Mix (Pie)│
└──────────────────────────────────────────────────────────┘
```

### Step-by-Step Creation

#### **Part 1: Create KPI Cards**

**Sheet 1: Total Revenue**
1. Create new worksheet → Name it "Total Revenue KPI"
2. Drag `Net Amount` from transactions_enhanced to Text
3. Change aggregation to SUM
4. Filter: `Is Won` = True
5. Format:
   - Right-click → Format → Numbers → Currency (Custom) → $0.0M
   - Increase font size to 48pt
   - Add label "Total Revenue" (size 18pt, gray color)
6. Hide axes and gridlines

**Sheet 2: Profit Margin**
1. Create new worksheet → "Profit Margin KPI"
2. Create calculated field:
   - Name: `Profit Margin %`
   - Formula: `SUM([Profit]) / SUM([Net Amount])`
3. Drag to Text
4. Format as Percentage (1 decimal)
5. Add conditional formatting:
   - Green if > 50%
   - Yellow if 40-50%
   - Red if < 40%

**Sheet 3: Active Customers**
1. Create new worksheet → "Active Customers KPI"
2. Drag `Customer Id` to Text
3. Change to COUNT(DISTINCT)
4. Filter by `Customer Segment` ≠ "Inactive"
5. Format as whole number with comma separator

#### **Part 2: Revenue Opportunities Chart**

**Sheet 4: Opportunity Breakdown**
1. Create new worksheet → "Revenue Opportunities"
2. From revenue_opportunities.csv:
   - Drag `Opportunity` to Rows
   - Drag `Revenue Impact` to Columns
3. Sort descending by Revenue Impact
4. Color by Priority:
   - High = Red/Orange
   - Medium = Yellow
5. Add labels showing dollar amounts
6. Format:
   - Bar color with gradient
   - Add reference line at $400K (target per opportunity)

#### **Part 3: Revenue Trend Line**

**Sheet 5: Monthly Revenue Trend**
1. Create new worksheet → "Revenue Trend"
2. Drag `Transaction Date` to Columns (change to Month)
3. Drag `Net Amount` to Rows (SUM)
4. Filter: `Is Won` = True
5. Add trend line (Analytics pane)
6. Add forecast for next 3 months
7. Format:
   - Line color: Blue
   - Add reference band showing target growth
   - Show moving average (3 months)

#### **Part 4: Customer Segment Distribution**

**Sheet 6: Segment Pie Chart**
1. Create new worksheet → "Segment Distribution"
2. From customer_insights:
   - Drag `Customer Segment` to Color
   - Drag `Customer Id` to Angle (COUNT)
3. Change mark type to Pie
4. Add labels with percentages
5. Color scheme:
   - Champions: Dark Green
   - Loyal: Light Green
   - Potential: Yellow
   - At Risk: Orange
   - Lost: Red

#### **Part 5: Assemble Dashboard**

1. Create new Dashboard → Name "Executive Summary"
2. Set size: 1920 x 1080 (HD)
3. Drag sheets in this order:
   - Top row: 3 KPI cards (equal width)
   - Middle: Opportunity chart (70% width)
   - Bottom left: Revenue trend (50% width)
   - Bottom right: Segment pie (50% width)
4. Add title: "Sales Intelligence - Executive Summary"
5. Add filters:
   - Date range (show/hide)
   - Customer segment
   - Region

---

## Dashboard 2: Customer Intelligence

### Objective
Deep dive into customer segmentation, CLV, and churn risk

### Key Visualizations

**Sheet 7: Customer Segment Performance**
1. Create new worksheet → "Segment Performance"
2. Rows: `Customer Segment`
3. Columns: `CLV` (AVG), `Total Revenue` (SUM), `Customer Id` (COUNT)
4. Create combined bar and line chart
5. Sort by Total Revenue descending

**Sheet 8: CLV Distribution**
1. Create new worksheet → "CLV Histogram"
2. Drag `CLV` to Columns
3. Create bins (Edit → Bins → $10,000 size)
4. Drag `Customer Id` to Rows (COUNT)
5. Format as histogram

**Sheet 9: Churn Risk Matrix**
1. Create new worksheet → "Churn vs CLV"
2. Create calculated field: `Risk Category`
   - Formula:
   ```
   IF [Churn Probability] > 0.7 AND [CLV] > 50000 THEN "High Risk - High Value"
   ELIF [Churn Probability] > 0.7 THEN "High Risk - Low Value"
   ELIF [CLV] > 50000 THEN "Low Risk - High Value"
   ELSE "Low Risk - Low Value"
   END
   ```
3. Drag `Churn Probability` to Columns
4. Drag `CLV` to Rows
5. Drag `Customer Id` to Detail
6. Color by Risk Category
7. Size by CLV
8. Add quadrant reference lines at 0.5 (churn) and median CLV

**Sheet 10: RFM Heat Map**
1. Create new worksheet → "RFM Analysis"
2. Drag `Recency` to Columns (create bins: 0-30, 31-90, 91-180, 180+)
3. Drag `Frequency` to Rows (create bins: 1-2, 3-5, 6-10, 10+)
4. Drag `Customer Id` to Color (COUNT)
5. Drag `Monetary` to Size (AVG)
6. Format as heat map with color gradient

**Assemble Dashboard 2**
- Top: Segment performance bar chart
- Left: CLV histogram
- Center: Churn risk matrix (largest)
- Right: RFM heat map

---

## Dashboard 3: Opportunity Explorer

### Objective
Actionable insights for each revenue opportunity

**Sheet 11: At-Risk Customers Table**
1. Create new worksheet → "At Risk List"
2. From at_risk_customers.csv
3. Show: Company Name, CLV, Churn Probability, Last Purchase, Segment
4. Sort by CLV descending
5. Add conditional formatting on Churn Probability
6. Make interactive (click to filter other views)

**Sheet 12: Cross-Sell Candidates**
1. Create new worksheet → "Cross-Sell Matrix"
2. Show: Company Name, Current Products (COUNT), Total Revenue, Recommended Products
3. Create calculated field: `Untapped Revenue Potential`
   - Formula: `[Total Revenue] * 0.30`
4. Color by potential value

**Sheet 13: Sales Process Funnel**
1. Create new worksheet → "Sales Funnel"
2. Drag `Stage` to Columns (order: Lead → Qualified → Proposal → Negotiation → Closed Won)
3. Drag `Transaction Id` to Rows (COUNT)
4. Create funnel chart
5. Show conversion rates between stages
6. Highlight bottlenecks in red

**Sheet 14: Geographic Performance**
1. Create new worksheet → "State Performance"
2. Drag `State` to map
3. Color by Revenue (SUM)
4. Size by Customer Count
5. Add labels for top 10 states
6. Create calculated field: `Below Median`
   - Formula: `SUM([Net Amount]) < WINDOW_MEDIAN(SUM([Net Amount]))`
7. Use to highlight underperforming states

**Assemble Dashboard 3**
- Top: Opportunity selector (parameter)
- Left column: Relevant customer list (changes based on selection)
- Center: Main visualization for selected opportunity
- Right: Key metrics and recommendations

---

## Dashboard 4: Sales Performance

### Objective
Track sales rep and team performance

**Sheet 15: Rep Leaderboard**
1. Create new worksheet → "Top Performers"
2. From sales_rep_performance
3. Rows: `Rep Name`
4. Columns: `Total Revenue`, `Deals Closed`, `Avg Deal Size`
5. Sort by Total Revenue
6. Add sparklines for monthly trends
7. Color code top 25%, middle 50%, bottom 25%

**Sheet 16: Regional Performance**
1. Create new worksheet → "Region Comparison"
2. Rows: `Region`
3. Columns: `Total Revenue` (SUM)
4. Add reference line at average
5. Show variance from average

**Sheet 17: Win Rate by Segment**
1. Create new worksheet → "Win Rate Analysis"
2. Create calculated field: `Win Rate`
   - Formula: `SUM([Is Won]) / COUNT([Transaction Id])`
3. Rows: `Segment`
4. Columns: `Win Rate`
5. Format as percentage
6. Add target line at 55%

**Sheet 18: Rep Performance Scatter**
1. Create new worksheet → "Performance Matrix"
2. Columns: `Deals Closed`
3. Rows: `Avg Deal Size`
4. Detail: `Rep Name`
5. Color by `Experience Years`
6. Size by `Total Revenue`
7. Add quadrant reference lines

**Assemble Dashboard 4**
- Top: Rep leaderboard table
- Middle left: Regional comparison
- Middle right: Win rate by segment
- Bottom: Performance scatter plot
- Add filters: Time period, Region, Experience level

---

## Dashboard 5: Product Analytics

### Objective
Product performance and recommendations

**Sheet 19: Product Revenue**
1. Create new worksheet → "Top Products"
2. From product_performance
3. Rows: `Product Name`
4. Columns: `Total Revenue`
5. Color by `Category`
6. Sort descending
7. Show top 15

**Sheet 20: Category Performance**
1. Create new worksheet → "Category Mix"
2. Rows: `Category`
3. Columns: `Total Revenue`, `Total Profit`, `Profit Margin`
4. Create bullet chart
5. Add targets for each metric

**Sheet 21: Product Affinity**
1. Create new worksheet → "Frequently Bought Together"
2. Create calculated field to find product pairs
3. Show: Product A, Product B, Times Bought Together
4. Create network diagram
5. Size by frequency

**Sheet 22: Product Lifecycle**
1. Create new worksheet → "Product Trends"
2. Rows: `Product Name` (top 10 by revenue)
3. Columns: `Transaction Date` (Month)
4. Values: `Units Sold`
5. Create area chart
6. Add trend lines

**Assemble Dashboard 5**
- Top: Category performance
- Middle left: Top products bar chart
- Middle right: Product lifecycle area chart
- Bottom: Product affinity network

---

## Advanced Features to Add

### 1. Parameters for Interactivity

**Date Range Parameter**
```
Name: Select Time Period
Data Type: String
List: Last 30 Days, Last 90 Days, Last 6 Months, Last Year, All Time
```

**Metric Selector Parameter**
```
Name: View By Metric
Data Type: String
List: Revenue, Profit, Customer Count, Deal Count
```

### 2. Calculated Fields Library

**YoY Growth**
```
(SUM([Net Amount]) - LOOKUP(SUM([Net Amount]), -12)) / LOOKUP(SUM([Net Amount]), -12)
```

**Customer Status**
```
IF [Days Since Last Purchase] <= 90 THEN "Active"
ELIF [Days Since Last Purchase] <= 180 THEN "Warm"
ELSE "Inactive"
END
```

**Deal Size Category**
```
IF [Net Amount] >= 50000 THEN "Enterprise"
ELIF [Net Amount] >= 20000 THEN "Mid-Market"
ELIF [Net Amount] >= 5000 THEN "Small"
ELSE "Micro"
END
```

**Revenue Bucket**
```
IF [Total Revenue] >= 100000 THEN "High Value"
ELIF [Total Revenue] >= 50000 THEN "Medium Value"
ELIF [Total Revenue] >= 10000 THEN "Low Value"
ELSE "Very Low"
END
```

### 3. Actions to Configure

**Filter Action**
- Source: Customer list on any dashboard
- Target: All dashboards
- Run on: Select
- Clear on: Click outside

**Highlight Action**
- Source: Scatter plots
- Target: Tables and charts
- Run on: Hover

**URL Action**
- Link customer names to CRM (if applicable)
- Link to detailed reports

### 4. Formatting Best Practices

**Color Palette**
- Primary: #1f77b4 (Blue)
- Success: #2ca02c (Green)
- Warning: #ff7f0e (Orange)
- Danger: #d62728 (Red)
- Neutral: #7f7f7f (Gray)

**Fonts**
- Title: 24pt, Bold, Dark Gray
- Subtitles: 18pt, Semibold, Medium Gray
- Body: 12pt, Regular, Dark Gray
- KPIs: 48pt, Bold, Brand Color

**Layout**
- Consistent padding: 10px
- Consistent spacing between elements
- Align elements to grid
- Use containers for grouping

### 5. Publishing Checklist

Before publishing:
- [ ] All filters work correctly
- [ ] All actions trigger properly
- [ ] Performance is acceptable (<5 second load time)
- [ ] Tooltips are informative
- [ ] Color blind safe palette used
- [ ] Mobile responsive (if needed)
- [ ] Data source credentials configured
- [ ] Extract refresh schedule set (if using extracts)

---

## Tips for Success

1. **Start Simple**: Build one sheet at a time, test it, then move on
2. **Use Containers**: Group related visualizations in horizontal/vertical containers
3. **Test Filters**: Always test that filters apply to correct worksheets
4. **Performance**: Use extracts instead of live connections for large datasets
5. **Naming**: Use clear, descriptive names for all sheets and dashboards
6. **Documentation**: Add comments in calculated fields to explain logic
7. **Iteration**: Show to stakeholders early and often, incorporate feedback

---

## Common Issues and Solutions

**Issue**: Dashboard loads slowly
**Solution**: 
- Use extracts instead of live connection
- Limit number of marks displayed
- Aggregate data before bringing into Tableau
- Hide unused fields

**Issue**: Filters not working across dashboards
**Solution**:
- Check "Apply to worksheets" setting
- Ensure field names match exactly
- Use dashboard actions instead

**Issue**: Dates showing incorrectly
**Solution**:
- Check data type in Data Source page
- Ensure date format is consistent
- Use DATEPARSE if needed

**Issue**: Colors not consistent
**Solution**:
- Edit colors and select "Assign Palette"
- Check for multiple fields on Color shelf
- Clear formatting and reapply

---

## Next Steps After Building

1. **Share with stakeholders** for feedback
2. **Set up scheduled refresh** if using extracts
3. **Create story** to walk through key insights
4. **Export to PDF/PowerPoint** for presentations
5. **Publish to Tableau Server/Public** for wider access
6. **Document insights** in accompanying report
7. **Create action items** based on opportunities identified

---

**Good luck building your dashboard! 🚀**
