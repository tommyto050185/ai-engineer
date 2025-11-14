✅ 1. Trực quan hóa cho mô hình hồi quy (Regression)
1. Scatter plot: y thật vs y dự đoán
Thấy mô hình dự đoán tốt không.
Nếu các điểm nằm gần đường chéo → mô hình tốt.

2. Residual plot (Residual vs Predicted)
Kiểm tra tính tuyến tính.
Tìm heteroscedasticity (phân phối phần dư không đều).

3. Histogram / KDE của residuals
Kiểm tra phân phối chuẩn của phần dư.

4. Q-Q Plot
Kiểm tra phần dư có tuân theo phân phối chuẩn không.

5. Feature importance / Coefficients plot
Hồi quy tuyến tính → vẽ hệ số (β1, β2...)
Random forest / XGBoost → biểu đồ importance.

6. Partial Dependence Plot (PDP)
Cho thấy 1 biến ảnh hưởng thế nào đến y.

7. SHAP summary plot
Một trong những biểu đồ giải thích mô hình mạnh nhất.

✅ 2. Trực quan hóa cho mô hình phân loại (Classification)
1. Confusion matrix
Trực quan nhất dùng đánh giá mô hình.
Cho thấy số TP, FP, FN, TN.

2. ROC Curve + AUC
Đánh giá mô hình theo nhiều ngưỡng.

3. Precision–Recall Curve
Quan trọng khi dữ liệu lệch (imbalanced).

4. Probability histogram
Xem phân bố xác suất dự đoán.

5. Feature importance / coefficients plot
Logistic regression → vẽ hệ số log-odds
Tree models → feature importance

6. SHAP summary plot
Xem biến nào ảnh hưởng mạnh nhất đến dự đoán.

7. Decision boundary (nếu có 2 features)
Vẽ ranh giới phân lớp.

✅ 3. Trực quan hóa cho mô hình cây và ensemble
1. Tree visualization (Decision Tree Plot)
Graphviz hoặc sklearn plot_tree.

2. Feature importance
Gần như bắt buộc để hiểu cây và forest.

3. SHAP dependence plot
Giải thích phi tuyến.

4. PDP and ICE plots
Hiểu từng biến tác động thế nào.

✅ 4. Trực quan hóa cho mô hình deep learning
1. Loss curve (train vs val)
Quan trọng để xem overfitting.

2. Accuracy curve
Dùng trong classification.

3. Confusion matrix
Bắt buộc cho classification.

4. Grad-CAM (cho CNN image)
Nổi bật vùng ảnh mà model chú ý.

5. Embedding visualization (t-SNE / UMAP)
Dùng để xem các vector đặc trưng.

🎯 Tổng hợp nhanh – checklist cho 1 model
Mục đích	Visualizations cần có
Đánh giá hiệu năng	Confusion matrix / R² plot / residual plot
Kiểm tra lỗi	Residual plot, error distribution
Giải thích mô hình	Feature importance, SHAP
Kiểm tra overfitting	Learning curves
Kiểm tra giả định mô hình	Q-Q plot, scatter residual

