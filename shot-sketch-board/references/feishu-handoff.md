# Feishu Handoff

Use this reference whenever the user wants storyboard sketches to be copied from Excel into Feishu Sheets.

## Key Rule

Do not promise that Excel embedded images are real cell contents.

In `.xlsx`, images inserted by common spreadsheet libraries are usually floating drawing objects anchored near cells. They may look like they are inside cells, but when copied into Feishu Sheets, the image objects often do not travel with the cell values.

## Required Delivery For Feishu

For Feishu collaboration, provide a multi-part handoff:

1. `.xlsx` workbook with sketch previews for local review.
2. Exported sketch image folder, one image per shot/state.
3. Sketch image zip package.
4. Text index columns in the workbook:
   - `草图文件`
   - `飞书复制说明`
5. HTML paste file where sketch images are inside `<td>` cells as inline `<img>` content.
6. Optional sketch-only HTML paste file for updating only the sketch column.

The HTML paste file is the best no-API workaround for Feishu copying because the image is part of table cell HTML rather than an Excel floating drawing object.

## Workbook Columns

Keep the production table's original `草图/画面` or `草图/画面备注` column as local visual preview.

Add these columns after the sketch column when preparing a Feishu version:

- `草图文件`: file name such as `SHOT_003_ROW015_28-32秒.png`.
- `飞书复制说明`: short text explaining which image to insert and what the sketch means.

These two columns are essential because plain text is reliable when copied to Feishu even if images are filtered.

## File Naming

Use stable shot-linked names:

```text
SHOT_001_ROW012_18-20秒.png
SHOT_002_ROW014_24-28秒.png
SHOT_003_ROW015_28-32秒.png
```

When a shot has multiple states, add state suffixes when possible:

```text
SHOT_012_ROW039_A_转场前.png
SHOT_012_ROW039_B_转场后.png
```

## HTML Paste Rules

Generate two HTML files when possible:

- Full table paste version: all columns plus inline sketch images.
- Sketch-only paste version: row number, shot, line, and inline sketch image.

Use base64 `data:image/...` images for maximum portability. If Feishu blocks base64 images on paste, fall back to uploading the exported PNG files or using the Feishu API.

## QA Checklist

Before delivery, verify:

- The original workbook remains unchanged.
- The Feishu version still has all original rows and columns.
- The workbook has `草图文件` and `飞书复制说明`.
- The number of exported image files equals the number of embedded sketch images.
- The HTML file contains the same number of `<img>` tags as exported images.
- The zip package contains all sketch images.

## Hard Fail

Fail the handoff if the only delivered artifact is an Excel file with floating images and no image index, no exported image folder, and no HTML/Feishu-ready alternative.
