package com.zichun2000.dsplab.lab

import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import java.util.Locale

@Composable
fun ResearchDashboard() {
    val context = LocalContext.current
    var refreshKey by remember { mutableStateOf(0) }
    var participantCode by remember { mutableStateOf("") }
    var pendingCsv by remember { mutableStateOf("") }
    var exportStatus by remember { mutableStateOf("") }
    val store = remember(context, refreshKey) { ExperimentRecordStore(context) }
    val records = remember(refreshKey) { store.loadAll() }
    val preRecord = records.lastOrNull { it.labId == "PRE_TEST" }
    val postRecord = records.lastOrNull { it.labId == "POST_TEST" }
    val pre = store.getAssessmentScore("PRE_TEST") ?: preRecord?.observation?.substringAfter("score=")?.substringBefore("/")?.toIntOrNull()
    val post = store.getAssessmentScore("POST_TEST") ?: postRecord?.observation?.substringAfter("score=")?.substringBefore("/")?.toIntOrNull()
    val maxScore = store.getAssessmentMax("POST_TEST") ?: store.getAssessmentMax("PRE_TEST") ?: LearningAssessment.prePostItems.size
    val labIds = listOf(
        "LAB01_SIGNALS",
        "LAB02_SAMPLING",
        "LAB03_CONVOLUTION",
        "LAB04_DFT",
        "LAB05_FIR"
    )
    val completedLabs = labIds.associateWith { id ->
        store.isLabCompleted(id) || records.any { it.labId == id }
    }
    val labCount = completedLabs.values.count { it }
    val latestLabRecords = labIds.associateWith { id -> records.lastOrNull { it.labId == id } }
    val participantReady = participantCode.trim().matches(Regex("[A-Za-z0-9_-]{2,20}"))

    val exportLauncher = rememberLauncherForActivityResult(
        contract = ActivityResultContracts.CreateDocument("text/csv")
    ) { uri ->
        if (uri == null) {
            exportStatus = "Export cancelled."
        } else {
            val success = runCatching {
                val stream = context.contentResolver.openOutputStream(uri)
                    ?: error("Unable to open export destination")
                stream.bufferedWriter(Charsets.UTF_8).use { writer ->
                    writer.write(pendingCsv)
                }
            }.isSuccess
            exportStatus = if (success) "Research CSV exported successfully." else "Unable to export CSV. Please try again."
        }
    }

    Column(
        Modifier.padding(horizontal = 16.dp, vertical = 12.dp).verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(10.dp)
    ) {
        Text("Research", style = MaterialTheme.typography.headlineSmall)
        Text("Local learning-study summary", style = MaterialTheme.typography.bodyMedium)

        Card(Modifier.fillMaxWidth()) {
            Column(Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(6.dp)) {
                Text("Assessment", style = MaterialTheme.typography.titleMedium)
                Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
                    Text("Pre-test")
                    Text(pre?.let { "$it / $maxScore" } ?: "Not recorded")
                }
                Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
                    Text("Post-test")
                    Text(post?.let { "$it / $maxScore" } ?: "Not recorded")
                }
                if (pre != null && post != null) {
                    val max = maxScore.toDouble()
                    val gain = if (max - pre > 0) (post - pre) / (max - pre) else 0.0
                    Text("Normalized learning gain <g>", style = MaterialTheme.typography.labelLarge)
                    Text("${"%.3f".format(gain)}", style = MaterialTheme.typography.headlineMedium)
                } else {
                    Text("Submit both assessments to calculate <g>.")
                }
            }
        }

        Card(Modifier.fillMaxWidth()) {
            Column(Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(5.dp)) {
                Text("Activity", style = MaterialTheme.typography.titleMedium)
                Text("Labs completed: $labCount / 5")
                labIds.forEachIndexed { index, id ->
                    val duration = latestLabRecords[id]?.parameters?.get("durationSeconds")?.toLongOrNull()
                    val durationText = duration?.let { " · ${it / 60} min ${it % 60} s" } ?: ""
                    Text("Lab ${index + 1}: ${if (completedLabs[id] == true) "✓" else "—"}$durationText")
                }
                Text("Recorded events: ${records.size}")
                Text("Pre-test record: ${if (preRecord != null || pre != null) "✓" else "—"}    Post-test record: ${if (postRecord != null || post != null) "✓" else "—"}")
                Text("Data remain on this device until you export a coded research file.")
            }
        }

        Button(onClick = { refreshKey++ }, modifier = Modifier.fillMaxWidth()) {
            Text("Refresh data")
        }

        Card(Modifier.fillMaxWidth()) {
            Column(Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                Text("Coded research export", style = MaterialTheme.typography.titleMedium)
                Text("Enter a study code such as S023. Do not enter a student name or ID number.")
                OutlinedTextField(
                    value = participantCode,
                    onValueChange = {
                        participantCode = it.take(20)
                        exportStatus = ""
                    },
                    modifier = Modifier.fillMaxWidth(),
                    singleLine = true,
                    label = { Text("Participant code") }
                )
                Text(if (participantReady) "Code ready" else "Use 2–20 letters, numbers, _ or -")
                Button(
                    onClick = {
                        val code = participantCode.trim()
                        pendingCsv = buildResearchCsv(
                            participantCode = code,
                            pre = pre,
                            post = post,
                            maxScore = maxScore,
                            completedLabs = completedLabs,
                            records = records,
                            labIds = labIds
                        )
                        exportStatus = ""
                        exportLauncher.launch("DSP_Research_${code}.csv")
                    },
                    enabled = participantReady,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Text("Export Research CSV")
                }
                if (exportStatus.isNotBlank()) Text(exportStatus)
            }
        }

        Card(Modifier.fillMaxWidth()) {
            Column(Modifier.padding(14.dp)) {
                Text("Research note", style = MaterialTheme.typography.titleMedium)
                Text("The exported file contains the study participant code, assessment scores, completion status, time on task, and the latest reflection from each lab.")
            }
        }
    }
}

private fun buildResearchCsv(
    participantCode: String,
    pre: Int?,
    post: Int?,
    maxScore: Int,
    completedLabs: Map<String, Boolean>,
    records: List<ExperimentRecord>,
    labIds: List<String>
): String {
    val latestLabRecords = labIds.map { id -> records.lastOrNull { it.labId == id } }
    val gain = if (pre != null && post != null && maxScore - pre > 0) {
        (post - pre).toDouble() / (maxScore - pre).toDouble()
    } else null

    val header = mutableListOf(
        "ParticipantCode",
        "PreScore",
        "PostScore",
        "MaxScore",
        "NormalizedGain",
        "LabsCompleted"
    )
    val row = mutableListOf(
        participantCode,
        pre?.toString().orEmpty(),
        post?.toString().orEmpty(),
        maxScore.toString(),
        gain?.let { String.format(Locale.US, "%.3f", it) }.orEmpty(),
        completedLabs.values.count { it }.toString()
    )

    labIds.forEachIndexed { index, id ->
        val record = latestLabRecords[index]
        header += "Lab${index + 1}Completed"
        header += "Lab${index + 1}DurationSec"
        header += "Lab${index + 1}SubmittedAt"
        header += "Lab${index + 1}Reflection"
        row += if (completedLabs[id] == true) "1" else "0"
        row += record?.parameters?.get("durationSeconds").orEmpty()
        row += record?.timestamp?.toString().orEmpty()
        row += record?.observation.orEmpty()
    }

    return buildString {
        appendLine(header.joinToString(",") { csvCell(it) })
        appendLine(row.joinToString(",") { csvCell(it) })
    }
}

private fun csvCell(value: String): String {
    val escaped = value.replace("\"", "\"\"")
    return "\"$escaped\""
}
