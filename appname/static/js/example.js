function setUpdateModal(exampleID, columns) {
    var updateForm = document.getElementById("updateExampleForm");
    updateForm.innerHTML += `<input type="hidden" value="${exampleID}" name="example_id">`;

    var updateFormTitle = document.getElementById("UpdateExampleFormLabel");
    updateFormTitle.innerHTML = `Update Example ${exampleID}`;

    for (var i=0; i < columns.length; i++) {
        if (columns[i] == "Edit" || columns[i] == "Id") {
            continue;
        }
        var columnData = document.getElementById(`${columns[i].toLowerCase()}Data${exampleID}`);
        var columnDataText = columnData.innerText;
        var columnUpdateInput = document.getElementById(`${columns[i].toLowerCase()}UpdateInput`);
        columnUpdateInput.setAttribute("value", columnDataText);
    }
}

function setDeleteModal(exampleID) {
    var deleteForm = document.getElementById("deleteExampleForm");
    deleteForm.innerHTML += `<input type="hidden" value="${exampleID}" name="example_id">`;

    var deleteFormTitle = document.getElementById("DeleteExampleFormLabel");
    deleteFormTitle.innerHTML = `Delete Example ${exampleID}`;
}

// https://www.w3schools.com/howto/howto_js_sort_table.asp
function sortTable(n) {
    var switching = true;
    var sortingDirection = "ascending";
    var table = document.getElementById("examplesTable");
    var rows, i, x, y, shouldSwitch, switchcount = 0;

    while (switching) {
        switching = false;
        rows = table.rows;

        for (i=1; i < (rows.length - 1); i++) {
            shouldSwitch = false;

            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];

            if (sortingDirection == "ascending") {
                if (n == 0) {
                    if (parseInt(x.innerHTML.replace(/\D/g, '')) > parseInt(y.innerHTML.replace(/\D/g, ''))) {
                        shouldSwitch = true;
                        break;
                    }
                } else {
                    if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                        shouldSwitch = true;
                        break;
                    }
                }
            } else if (sortingDirection == "descending") {
                if (n == 0) {
                    if (parseInt(x.innerHTML.replace(/\D/g, '')) < parseInt(y.innerHTML.replace(/\D/g, ''))) {
                        shouldSwitch = true;
                        break;
                    }
                } else {
                    if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                        shouldSwitch = true;
                        break;
                    }
                }
            }
        }
        
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount++;
        } else {
            if (switchcount == 0 && sortingDirection == "ascending") {
                sortingDirection = "descending";
                switching = true;
            }
        }
    }
}
