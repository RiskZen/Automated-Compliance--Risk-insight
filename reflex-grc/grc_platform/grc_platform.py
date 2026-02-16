"""Main GRC Platform Application - Pure Python with Reflex"""
import reflex as rx
from typing import Dict, Any
from .state import (
    GRCState, FrameworkState, ControlState, PolicyState, RiskState,
    TestingState, IssueState, KRIState, KCIState, HeatmapState
)

# Sidebar Component
def sidebar() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Logo
            rx.hstack(
                rx.icon("sparkles", size=28, color="#60a5fa"),
                rx.vstack(
                    rx.text("GRC Platform", font_size="20px", font_weight="bold", color="white"),
                    rx.text("Pure Python Edition", font_size="12px", color="#94a3b8"),
                    spacing="0",
                    align_items="start"
                ),
                spacing="3",
                padding="20px"
            ),
            
            # Navigation
            rx.vstack(
                rx.text("OVERVIEW", font_size="11px", color="#64748b", font_weight="600", padding_left="15px", margin_top="20px"),
                rx.link(
                    rx.hstack(
                        rx.icon("layout-dashboard", size=20),
                        rx.text("Dashboard", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                
                rx.text("FRAMEWORK & CONTROLS", font_size="11px", color="#64748b", font_weight="600", padding_left="15px", margin_top="20px"),
                rx.link(
                    rx.hstack(
                        rx.icon("shield", size=20),
                        rx.text("Frameworks", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/frameworks",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                rx.link(
                    rx.hstack(
                        rx.icon("git-branch", size=20),
                        rx.text("Control Mapping", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/controls",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                rx.link(
                    rx.hstack(
                        rx.icon("file-text", size=20),
                        rx.text("Policies", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/policies",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                
                rx.text("TESTING & ISSUES", font_size="11px", color="#64748b", font_weight="600", padding_left="15px", margin_top="20px"),
                rx.link(
                    rx.hstack(
                        rx.icon("clipboard-check", size=20),
                        rx.text("Control Testing", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/testing",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                rx.link(
                    rx.hstack(
                        rx.icon("triangle-alert", size=20),
                        rx.text("Issues", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/issues",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                
                rx.text("RISK MANAGEMENT", font_size="11px", color="#64748b", font_weight="600", padding_left="15px", margin_top="20px"),
                rx.link(
                    rx.hstack(
                        rx.icon("trending-up", size=20),
                        rx.text("Risks", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/risks",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                rx.link(
                    rx.hstack(
                        rx.icon("bar-chart-3", size=20),
                        rx.text("KRIs", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/kris",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                rx.link(
                    rx.hstack(
                        rx.icon("target", size=20),
                        rx.text("KCIs", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/kcis",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                rx.link(
                    rx.hstack(
                        rx.icon("flame", size=20),
                        rx.text("Risk Heatmap", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/heatmap",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                
                spacing="2",
                width="100%",
                padding="10px"
            ),
            
            # Footer
            rx.box(
                rx.box(
                    rx.text("Production Ready", font_size="11px", color="#94a3b8", margin_bottom="5px"),
                    rx.text("Complete GRC Platform", font_size="13px", color="#e2e8f0", font_weight="600"),
                    padding="15px",
                    bg="#1e293b",
                    border_radius="8px",
                    border="1px solid #334155"
                ),
                padding="15px",
                margin_top="auto"
            ),
            
            height="100vh",
            spacing="0",
            position="fixed",
            left="0",
            top="0",
            width="260px",
            bg="#0f172a",
            overflow_y="auto"
        )
    )

# Layout wrapper
def layout(page_content: rx.Component) -> rx.Component:
    return rx.box(
        sidebar(),
        rx.box(
            page_content,
            margin_left="260px",
            padding="40px",
            bg="#f8fafc",
            min_height="100vh"
        )
    )

# Dashboard Page
@rx.page(route="/", title="Dashboard - GRC Platform", on_load=GRCState.load_all_data)
def dashboard() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("GRC Dashboard", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Real-time compliance and risk management overview", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            # Metrics Grid
            rx.grid(
                # Enabled Frameworks
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.icon("shield", size=24, color="#3b82f6"),
                            bg="#eff6ff",
                            padding="10px",
                            border_radius="50%"
                        ),
                        justify="between",
                        width="100%",
                        margin_bottom="15px"
                    ),
                    rx.text("Enabled Frameworks", font_size="14px", color="#64748b", margin_bottom="5px"),
                    rx.text(GRCState.enabled_frameworks, font_size="36px", font_weight="bold", color="#0f172a"),
                    rx.text(GRCState.total_unified_controls.to_string() + " unified controls", font_size="12px", color="#64748b", margin_top="5px"),
                    bg="white",
                    padding="24px",
                    border_radius="12px",
                    border="1px solid #e2e8f0",
                    box_shadow="sm"
                ),
                
                # Control Effectiveness
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.icon("circle-check", size=24, color="#10b981"),
                            bg="#f0fdf4",
                            padding="10px",
                            border_radius="50%"
                        ),
                        justify="between",
                        width="100%",
                        margin_bottom="15px"
                    ),
                    rx.text("Control Effectiveness", font_size="14px", color="#64748b", margin_bottom="5px"),
                    rx.text(GRCState.control_effectiveness.to_string() + "%", font_size="36px", font_weight="bold", color="#0f172a"),
                    rx.text(GRCState.passed_tests.to_string() + " of " + GRCState.total_tests.to_string() + " passed", font_size="12px", color="#10b981", margin_top="5px"),
                    bg="white",
                    padding="24px",
                    border_radius="12px",
                    border="1px solid #e2e8f0",
                    box_shadow="sm"
                ),
                
                # Open Issues
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.icon("triangle-alert", size=24, color="#ef4444"),
                            bg="#fef2f2",
                            padding="10px",
                            border_radius="50%"
                        ),
                        justify="between",
                        width="100%",
                        margin_bottom="15px"
                    ),
                    rx.text("Open Issues", font_size="14px", color="#64748b", margin_bottom="5px"),
                    rx.text(GRCState.open_issues, font_size="36px", font_weight="bold", color="#0f172a"),
                    rx.text(GRCState.total_issues.to_string() + " total issues", font_size="12px", color="#64748b", margin_top="5px"),
                    bg="white",
                    padding="24px",
                    border_radius="12px",
                    border="1px solid #e2e8f0",
                    box_shadow="sm"
                ),
                
                # Average Risk
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.icon("bar-chart-3", size=24, color="#f59e0b"),
                            bg="#fffbeb",
                            padding="10px",
                            border_radius="50%"
                        ),
                        justify="between",
                        width="100%",
                        margin_bottom="15px"
                    ),
                    rx.text("Average Risk Score", font_size="14px", color="#64748b", margin_bottom="5px"),
                    rx.text(GRCState.avg_residual_risk, font_size="36px", font_weight="bold", color="#0f172a"),
                    rx.text(GRCState.total_risks.to_string() + " risks tracked", font_size="12px", color="#64748b", margin_top="5px"),
                    bg="white",
                    padding="24px",
                    border_radius="12px",
                    border="1px solid #e2e8f0",
                    box_shadow="sm"
                ),
                
                columns="4",
                spacing="6",
                width="100%",
                margin_bottom="30px"
            ),
            
            # Info Section
            rx.box(
                rx.heading("Welcome to GRC Platform", font_size="24px", margin_bottom="10px", color="#0f172a"),
                rx.text(
                    "This is a complete GRC automation platform built in pure Python using Reflex and powered by Google Gemini AI.",
                    font_size="16px",
                    color="#64748b",
                    margin_bottom="20px"
                ),
                rx.text("Features:", font_weight="600", margin_bottom="10px", color="#0f172a"),
                rx.unordered_list(
                    rx.list_item("5 Compliance Frameworks (ISO 27001, PCI-DSS, SOC2, NIST, GDPR)"),
                    rx.list_item("Map Once, Comply Many - Unified control framework"),
                    rx.list_item("AI-Powered Risk Suggestions with Google Gemini"),
                    rx.list_item("Control Testing with Evidence Upload"),
                    rx.list_item("Issue Lifecycle Management"),
                    rx.list_item("Dynamic Risk→KRI→KCI→Control Mapping"),
                    color="#64748b",
                    spacing="2"
                ),
                bg="white",
                padding="30px",
                border_radius="12px",
                border="1px solid #e2e8f0",
                box_shadow="sm"
            ),
            
            spacing="6",
            width="100%"
        )
    )

# Framework Management Page
@rx.page(route="/frameworks", title="Frameworks - GRC Platform", on_load=FrameworkState.load_all_data)
def frameworks() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Framework Management", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Select compliance frameworks to map and manage", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            rx.cond(
                FrameworkState.loading,
                rx.center(
                    rx.spinner(size="3"),
                    padding="100px"
                ),
                rx.vstack(
                    rx.foreach(
                        FrameworkState.frameworks,
                        lambda fw: rx.box(
                            rx.hstack(
                                rx.vstack(
                                    rx.hstack(
                                        rx.box(
                                            rx.icon("shield", size=24, color=rx.cond(fw["enabled"], "#3b82f6", "#64748b")),
                                            bg=rx.cond(fw["enabled"], "#eff6ff", "#f1f5f9"),
                                            padding="12px",
                                            border_radius="8px"
                                        ),
                                        rx.vstack(
                                            rx.text(fw["name"], font_size="20px", font_weight="bold", color="#0f172a"),
                                            rx.text("Version " + fw["version"].to_string(), font_size="14px", color="#64748b"),
                                            spacing="0",
                                            align_items="start"
                                        ),
                                        rx.cond(
                                            fw["enabled"],
                                            rx.badge("Enabled", color_scheme="green"),
                                            rx.fragment()
                                        ),
                                        spacing="3"
                                    ),
                                    rx.text(fw["description"], font_size="15px", color="#64748b", margin_top="10px"),
                                    rx.text(fw["total_controls"].to_string() + " controls", font_size="14px", color="#64748b", font_weight="600", margin_top="10px"),
                                    align_items="start",
                                    flex="1"
                                ),
                                rx.button(
                                    rx.cond(
                                        fw["enabled"],
                                        "Disable",
                                        "Enable"
                                    ),
                                    on_click=FrameworkState.toggle_framework(fw["id"]),
                                    bg=rx.cond(fw["enabled"], "#ef4444", "#3b82f6"),
                                    color="white",
                                    _hover={"opacity": 0.8},
                                    padding="12px 24px",
                                    border_radius="8px",
                                    font_weight="600"
                                ),
                                width="100%",
                                align_items="start"
                            ),
                            bg="white",
                            padding="24px",
                            border_radius="12px",
                            border=rx.cond(fw["enabled"], "2px solid #3b82f6", "1px solid #e2e8f0"),
                            box_shadow="sm",
                            margin_bottom="20px",
                            _hover={"box_shadow": "md"}
                        )
                    ),
                    width="100%"
                )
            ),
            
            spacing="6",
            width="100%"
        )
    )


# Control Mapping Page - Simplified with expandable details
@rx.page(route="/controls", title="Control Mapping - GRC Platform", on_load=ControlState.load_all_data)
def controls() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Control Mapping", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Map framework controls → Unified CCF → Internal policies", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            # Info Banner
            rx.box(
                rx.hstack(
                    rx.icon("info", size=20, color="#3b82f6"),
                    rx.text(
                        "Click 'View Mapping' on any control to see the detailed mapping flow from Framework Controls → Unified Control → Policies",
                        font_size="14px",
                        color="#1e40af"
                    ),
                    spacing="3",
                    align_items="center"
                ),
                bg="#eff6ff",
                padding="15px 20px",
                border_radius="10px",
                border="1px solid #bfdbfe",
                margin_bottom="25px"
            ),
            
            # Create Control Section
            rx.box(
                rx.hstack(
                    rx.heading("Unified Controls (CCF)", font_size="24px", font_weight="600"),
                    rx.button(
                        rx.icon("plus", size=20),
                        " Create Control",
                        on_click=ControlState.toggle_create_form,
                        bg="#3b82f6",
                        color="white",
                        _hover={"bg": "#2563eb"},
                        padding="12px 20px",
                        border_radius="8px",
                        font_weight="600"
                    ),
                    justify="between",
                    width="100%",
                    margin_bottom="20px"
                ),
                
                # Create Form
                rx.cond(
                    ControlState.show_create_form,
                    rx.box(
                        rx.vstack(
                            rx.input(
                                placeholder="CCF ID (e.g., CCF-AC-001)",
                                value=ControlState.new_control_ccf_id,
                                on_change=ControlState.set_new_control_ccf_id,
                                width="100%"
                            ),
                            rx.input(
                                placeholder="Control Name",
                                value=ControlState.new_control_name,
                                on_change=ControlState.set_new_control_name,
                                width="100%"
                            ),
                            rx.text_area(
                                placeholder="Description",
                                value=ControlState.new_control_description,
                                on_change=ControlState.set_new_control_description,
                                width="100%"
                            ),
                            rx.select(
                                ["Preventive", "Detective", "Corrective"],
                                value=ControlState.new_control_type,
                                on_change=ControlState.set_new_control_type,
                                width="100%"
                            ),
                            rx.input(
                                placeholder="Owner",
                                value=ControlState.new_control_owner,
                                on_change=ControlState.set_new_control_owner,
                                width="100%"
                            ),
                            rx.hstack(
                                rx.button(
                                    "Create Control",
                                    on_click=ControlState.create_control,
                                    bg="#3b82f6",
                                    color="white",
                                    _hover={"bg": "#2563eb"}
                                ),
                                rx.button(
                                    "Cancel",
                                    on_click=ControlState.toggle_create_form,
                                    bg="#e2e8f0",
                                    color="#0f172a"
                                ),
                                spacing="3"
                            ),
                            spacing="4",
                            width="100%"
                        ),
                        bg="#f8fafc",
                        padding="20px",
                        border_radius="8px",
                        margin_bottom="20px"
                    ),
                    rx.fragment()
                ),
                
                # Controls List with Expandable Mapping Details
                rx.foreach(
                    ControlState.unified_controls,
                    lambda ctrl: rx.box(
                        rx.vstack(
                            # Control Header
                            rx.hstack(
                                rx.vstack(
                                    rx.hstack(
                                        rx.badge(ctrl["ccf_id"], color_scheme="blue", font_family="monospace"),
                                        rx.text(ctrl["name"], font_size="18px", font_weight="600", color="#0f172a"),
                                        spacing="3"
                                    ),
                                    rx.text(ctrl["description"], font_size="14px", color="#64748b", margin_top="8px"),
                                    rx.hstack(
                                        rx.text("Type: " + ctrl["control_type"].to_string(), font_size="13px", color="#64748b"),
                                        rx.text("Frequency: " + ctrl["frequency"].to_string(), font_size="13px", color="#64748b"),
                                        rx.text("Owner: " + ctrl["owner"].to_string(), font_size="13px", color="#64748b"),
                                        spacing="5",
                                        margin_top="10px"
                                    ),
                                    align_items="start",
                                    flex="1"
                                ),
                                # Toggle Button for Mapping Details
                                rx.button(
                                    rx.cond(
                                        ControlState.expanded_controls.contains(ctrl["id"]),
                                        rx.hstack(
                                            rx.icon("chevron-up", size=18),
                                            rx.text("Hide Mapping"),
                                            spacing="2"
                                        ),
                                        rx.hstack(
                                            rx.icon("chevron-down", size=18),
                                            rx.text("View Mapping"),
                                            spacing="2"
                                        )
                                    ),
                                    on_click=ControlState.toggle_control_details(ctrl["id"]),
                                    bg=rx.cond(
                                        ControlState.expanded_controls.contains(ctrl["id"]),
                                        "#f0fdf4",
                                        "#f8fafc"
                                    ),
                                    color=rx.cond(
                                        ControlState.expanded_controls.contains(ctrl["id"]),
                                        "#10b981",
                                        "#64748b"
                                    ),
                                    border=rx.cond(
                                        ControlState.expanded_controls.contains(ctrl["id"]),
                                        "1px solid #86efac",
                                        "1px solid #e2e8f0"
                                    ),
                                    _hover={"bg": "#f0fdf4", "color": "#10b981"},
                                    padding="10px 16px",
                                    border_radius="8px",
                                    font_weight="500",
                                    font_size="13px"
                                ),
                                width="100%",
                                align_items="start"
                            ),
                            
                            align_items="start",
                            width="100%"
                        ),
                        bg="white",
                        padding="20px",
                        border_radius="12px",
                        border=rx.cond(
                            ControlState.expanded_controls.contains(ctrl["id"]),
                            "2px solid #10b981",
                            "1px solid #e2e8f0"
                        ),
                        margin_bottom="15px",
                        _hover={"box_shadow": "md"},
                        transition="all 0.2s ease"
                    )
                ),
                
                # Mapping Details Panel (shown when a control is expanded)
                rx.cond(
                    ControlState.selected_control_id != "",
                    rx.box(
                        rx.vstack(
                            # Header
                            rx.hstack(
                                rx.icon("git-branch", size=24, color="#8b5cf6"),
                                rx.text("Mapping Details for: ", font_size="18px", font_weight="600", color="#0f172a"),
                                rx.badge(ControlState.selected_control_mappings["ccf_id"], color_scheme="green", font_family="monospace", font_size="16px"),
                                spacing="3"
                            ),
                            
                            # Visual Flow
                            rx.box(
                                rx.hstack(
                                    # Framework Controls
                                    rx.vstack(
                                        rx.hstack(
                                            rx.icon("shield", size=20, color="#3b82f6"),
                                            rx.text("Framework Controls", font_size="14px", font_weight="600", color="#3b82f6"),
                                            spacing="2"
                                        ),
                                        rx.box(
                                            rx.text(ControlState.selected_control_mappings["framework_controls_text"], 
                                                   font_size="13px", color="#64748b", white_space="pre-wrap"),
                                            bg="#eff6ff",
                                            padding="15px",
                                            border_radius="8px",
                                            border="1px solid #bfdbfe",
                                            width="100%",
                                            min_height="100px"
                                        ),
                                        rx.badge(ControlState.selected_control_mappings["framework_controls_count"].to_string() + " mapped", color_scheme="blue"),
                                        bg="white",
                                        padding="20px",
                                        border_radius="12px",
                                        border="1px solid #e2e8f0",
                                        min_width="280px",
                                        align_items="start",
                                        spacing="3"
                                    ),
                                    
                                    # Arrow 1
                                    rx.vstack(
                                        rx.icon("arrow-right", size=32, color="#10b981"),
                                        rx.text("maps to", font_size="12px", color="#64748b"),
                                        spacing="2",
                                        align_items="center",
                                        padding_x="20px"
                                    ),
                                    
                                    # Unified Control (Center)
                                    rx.vstack(
                                        rx.hstack(
                                            rx.icon("target", size=20, color="#10b981"),
                                            rx.text("Unified Control", font_size="14px", font_weight="600", color="#10b981"),
                                            spacing="2"
                                        ),
                                        rx.box(
                                            rx.vstack(
                                                rx.badge(ControlState.selected_control_mappings["ccf_id"], color_scheme="green", font_family="monospace", font_size="14px"),
                                                rx.text(ControlState.selected_control_mappings["name"], font_size="14px", font_weight="600", color="#0f172a", text_align="center"),
                                                rx.text("Type: " + ControlState.selected_control_mappings["control_type"].to_string(), font_size="12px", color="#64748b"),
                                                spacing="3",
                                                align_items="center"
                                            ),
                                            bg="#f0fdf4",
                                            padding="20px",
                                            border_radius="8px",
                                            border="2px solid #86efac"
                                        ),
                                        bg="white",
                                        padding="20px",
                                        border_radius="12px",
                                        border="2px solid #10b981",
                                        min_width="220px",
                                        align_items="center",
                                        spacing="3"
                                    ),
                                    
                                    # Arrow 2
                                    rx.vstack(
                                        rx.icon("arrow-right", size=32, color="#8b5cf6"),
                                        rx.text("implements", font_size="12px", color="#64748b"),
                                        spacing="2",
                                        align_items="center",
                                        padding_x="20px"
                                    ),
                                    
                                    # Policies
                                    rx.vstack(
                                        rx.hstack(
                                            rx.icon("file-text", size=20, color="#8b5cf6"),
                                            rx.text("Internal Policies", font_size="14px", font_weight="600", color="#8b5cf6"),
                                            spacing="2"
                                        ),
                                        rx.box(
                                            rx.text(ControlState.selected_control_mappings["policies_text"], 
                                                   font_size="13px", color="#64748b", white_space="pre-wrap"),
                                            bg="#faf5ff",
                                            padding="15px",
                                            border_radius="8px",
                                            border="1px solid #e9d5ff",
                                            width="100%",
                                            min_height="100px"
                                        ),
                                        rx.badge(ControlState.selected_control_mappings["policies_count"].to_string() + " mapped", color_scheme="purple"),
                                        bg="white",
                                        padding="20px",
                                        border_radius="12px",
                                        border="1px solid #e2e8f0",
                                        min_width="280px",
                                        align_items="start",
                                        spacing="3"
                                    ),
                                    
                                    spacing="4",
                                    align_items="center",
                                    justify="center",
                                    width="100%",
                                    padding="20px"
                                ),
                                bg="#fafafa",
                                padding="20px",
                                border_radius="12px",
                                margin_top="20px"
                            ),
                            
                            # Automation Badge
                            rx.cond(
                                ControlState.selected_control_mappings["automation_possible"],
                                rx.hstack(
                                    rx.icon("zap", size=18, color="#f59e0b"),
                                    rx.text("This control is automation ready", font_size="14px", color="#92400e"),
                                    spacing="2",
                                    bg="#fffbeb",
                                    padding="10px 15px",
                                    border_radius="8px",
                                    border="1px solid #fcd34d",
                                    margin_top="15px"
                                ),
                                rx.fragment()
                            ),
                            
                            spacing="4",
                            width="100%",
                            align_items="start"
                        ),
                        bg="white",
                        padding="30px",
                        border_radius="12px",
                        border="2px solid #8b5cf6",
                        box_shadow="lg",
                        margin_top="20px"
                    ),
                    rx.fragment()
                ),
                
                bg="white",
                padding="30px",
                border_radius="12px",
                border="1px solid #e2e8f0",
                box_shadow="sm"
            ),
            
            spacing="6",
            width="100%"
        )
    )


# Policies Page
@rx.page(route="/policies", title="Policies - GRC Platform", on_load=PolicyState.load_all_data)
def policies() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Policy Management", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Manage internal policies and map to controls", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            rx.box(
                rx.hstack(
                    rx.heading("Internal Policies", font_size="24px", font_weight="600"),
                    rx.button(
                        rx.icon("plus", size=20),
                        " Create Policy",
                        on_click=PolicyState.toggle_policy_form,
                        bg="#3b82f6",
                        color="white",
                        _hover={"bg": "#2563eb"}
                    ),
                    justify="between",
                    width="100%",
                    margin_bottom="20px"
                ),
                
                # Create Form
                rx.cond(
                    PolicyState.show_policy_form,
                    rx.box(
                        rx.vstack(
                            rx.input(placeholder="Policy ID (e.g., POL-SEC-100)", value=PolicyState.new_policy_id, on_change=PolicyState.set_new_policy_id, width="100%"),
                            rx.input(placeholder="Policy Name", value=PolicyState.new_policy_name, on_change=PolicyState.set_new_policy_name, width="100%"),
                            rx.text_area(placeholder="Description", value=PolicyState.new_policy_description, on_change=PolicyState.set_new_policy_description, width="100%"),
                            rx.input(placeholder="Owner", value=PolicyState.new_policy_owner, on_change=PolicyState.set_new_policy_owner, width="100%"),
                            rx.hstack(
                                rx.button("Create Policy", on_click=PolicyState.create_policy, bg="#3b82f6", color="white"),
                                rx.button("Cancel", on_click=PolicyState.toggle_policy_form, bg="#e2e8f0"),
                                spacing="3"
                            ),
                            spacing="4"
                        ),
                        bg="#f8fafc",
                        padding="20px",
                        border_radius="8px",
                        margin_bottom="20px"
                    ),
                    rx.fragment()
                ),
                
                # Policies List
                rx.foreach(
                    PolicyState.policies,
                    lambda pol: rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.badge(pol["policy_id"], color_scheme="purple", font_family="monospace"),
                                rx.text(pol["name"], font_size="18px", font_weight="600"),
                                rx.badge(pol["status"], color_scheme="green"),
                                spacing="3"
                            ),
                            rx.text(pol["description"], font_size="14px", color="#64748b", margin_top="8px"),
                            rx.text("Category: " + pol["category"].to_string() + " | Owner: " + pol["owner"].to_string(), font_size="13px", color="#64748b", margin_top="8px"),
                            align_items="start"
                        ),
                        bg="white",
                        padding="20px",
                        border_radius="12px",
                        border="1px solid #e2e8f0",
                        margin_bottom="15px"
                    )
                ),
                
                bg="white",
                padding="30px",
                border_radius="12px",
                border="1px solid #e2e8f0"
            ),
            
            spacing="6",
            width="100%"
        )
    )

# Risks Page with AI
@rx.page(route="/risks", title="Risk Management - GRC Platform", on_load=RiskState.load_all_data)
def risks() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Risk Management", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Manage risks with AI-powered insights from Google Gemini", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            # AI Banner
            rx.box(
                rx.hstack(
                    rx.box(
                        rx.icon("sparkles", size=32, color="white"),
                        bg="white",
                        bg_clip="padding-box",
                        padding="12px",
                        border_radius="50%"
                    ),
                    rx.vstack(
                        rx.text("AI-Powered Risk Suggestions", font_size="20px", font_weight="bold", color="white"),
                        rx.text("Let Google Gemini suggest top 10 risks", font_size="14px", color="rgba(255,255,255,0.9)"),
                        spacing="1",
                        align_items="start"
                    ),
                    rx.button(
                        rx.cond(
                            RiskState.loading_ai,
                            rx.spinner(size="2"),
                            rx.hstack(
                                rx.icon("brain", size=20),
                                rx.text("Get AI Suggestions"),
                                spacing="2"
                            )
                        ),
                        on_click=RiskState.get_ai_risk_suggestions,
                        bg="white",
                        color="#3b82f6",
                        _hover={"bg": "rgba(255,255,255,0.9)"},
                        padding="12px 24px",
                        border_radius="8px",
                        font_weight="600"
                    ),
                    justify="between",
                    align_items="center",
                    width="100%"
                ),
                background="linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%)",
                padding="30px",
                border_radius="12px",
                margin_bottom="30px"
            ),
            
            # Create Risk
            rx.box(
                rx.hstack(
                    rx.heading("Risks", font_size="24px", font_weight="600"),
                    rx.button(
                        rx.icon("plus", size=20),
                        " Add Risk",
                        on_click=RiskState.toggle_risk_form,
                        bg="#3b82f6",
                        color="white"
                    ),
                    justify="between",
                    width="100%",
                    margin_bottom="20px"
                ),
                
                # Risks List
                rx.foreach(
                    RiskState.risks,
                    lambda risk: rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.text(risk["name"], font_size="18px", font_weight="600"),
                                rx.badge(risk["category"], color_scheme="blue"),
                                spacing="3"
                            ),
                            rx.text(risk["description"], font_size="14px", color="#64748b"),
                            rx.hstack(
                                rx.vstack(
                                    rx.text("Inherent Risk", font_size="12px", color="#64748b"),
                                    rx.text(risk["inherent_risk_score"], font_size="20px", font_weight="bold", color="#ef4444"),
                                    spacing="0"
                                ),
                                rx.vstack(
                                    rx.text("Residual Risk", font_size="12px", color="#64748b"),
                                    rx.text(risk["residual_risk_score"], font_size="20px", font_weight="bold", color="#10b981"),
                                    spacing="0"
                                ),
                                rx.vstack(
                                    rx.text("Owner", font_size="12px", color="#64748b"),
                                    rx.text(risk["owner"], font_size="14px", font_weight="600"),
                                    spacing="0"
                                ),
                                spacing="8",
                                margin_top="15px"
                            ),
                            align_items="start"
                        ),
                        bg="white",
                        padding="20px",
                        border_radius="12px",
                        border="1px solid #e2e8f0",
                        margin_bottom="15px"
                    )
                ),
                
                bg="white",
                padding="30px",
                border_radius="12px",
                border="1px solid #e2e8f0"
            ),
            
            spacing="6",
            width="100%"
        )
    )


# Control Testing Page
@rx.page(route="/testing", title="Control Testing - GRC Platform", on_load=TestingState.load_all_data)
def testing() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Control Testing", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Schedule and record control tests with evidence", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            # Stats Cards
            rx.grid(
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.icon("clipboard-check", size=24, color="#10b981"),
                            bg="#f0fdf4",
                            padding="10px",
                            border_radius="50%"
                        ),
                        rx.vstack(
                            rx.text("Total Tests", font_size="14px", color="#64748b"),
                            rx.text(TestingState.total_tests, font_size="28px", font_weight="bold", color="#0f172a"),
                            spacing="0",
                            align_items="start"
                        ),
                        spacing="4"
                    ),
                    bg="white",
                    padding="20px",
                    border_radius="12px",
                    border="1px solid #e2e8f0"
                ),
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.icon("circle-check", size=24, color="#10b981"),
                            bg="#f0fdf4",
                            padding="10px",
                            border_radius="50%"
                        ),
                        rx.vstack(
                            rx.text("Passed", font_size="14px", color="#64748b"),
                            rx.text(TestingState.passed_tests, font_size="28px", font_weight="bold", color="#10b981"),
                            spacing="0",
                            align_items="start"
                        ),
                        spacing="4"
                    ),
                    bg="white",
                    padding="20px",
                    border_radius="12px",
                    border="1px solid #e2e8f0"
                ),
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.icon("x-circle", size=24, color="#ef4444"),
                            bg="#fef2f2",
                            padding="10px",
                            border_radius="50%"
                        ),
                        rx.vstack(
                            rx.text("Failed", font_size="14px", color="#64748b"),
                            rx.text((TestingState.total_tests - TestingState.passed_tests), font_size="28px", font_weight="bold", color="#ef4444"),
                            spacing="0",
                            align_items="start"
                        ),
                        spacing="4"
                    ),
                    bg="white",
                    padding="20px",
                    border_radius="12px",
                    border="1px solid #e2e8f0"
                ),
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.icon("percent", size=24, color="#3b82f6"),
                            bg="#eff6ff",
                            padding="10px",
                            border_radius="50%"
                        ),
                        rx.vstack(
                            rx.text("Effectiveness", font_size="14px", color="#64748b"),
                            rx.text(TestingState.control_effectiveness.to_string() + "%", font_size="28px", font_weight="bold", color="#3b82f6"),
                            spacing="0",
                            align_items="start"
                        ),
                        spacing="4"
                    ),
                    bg="white",
                    padding="20px",
                    border_radius="12px",
                    border="1px solid #e2e8f0"
                ),
                columns="4",
                spacing="4",
                width="100%",
                margin_bottom="30px"
            ),
            
            # Test Records Section
            rx.box(
                rx.hstack(
                    rx.heading("Test Records", font_size="24px", font_weight="600"),
                    rx.button(
                        rx.icon("plus", size=20),
                        " Record Test",
                        on_click=TestingState.toggle_test_form,
                        bg="#3b82f6",
                        color="white",
                        _hover={"bg": "#2563eb"},
                        padding="12px 20px",
                        border_radius="8px",
                        font_weight="600"
                    ),
                    justify="between",
                    width="100%",
                    margin_bottom="20px"
                ),
                
                # Create Form
                rx.cond(
                    TestingState.show_test_form,
                    rx.box(
                        rx.vstack(
                            rx.input(
                                placeholder="Control ID (e.g., ctrl-001)",
                                value=TestingState.new_test_control_id,
                                on_change=TestingState.set_new_test_control_id,
                                width="100%"
                            ),
                            rx.input(
                                placeholder="Tester Name",
                                value=TestingState.new_test_tester,
                                on_change=TestingState.set_new_test_tester,
                                width="100%"
                            ),
                            rx.input(
                                placeholder="Test Date (YYYY-MM-DD)",
                                value=TestingState.new_test_date,
                                on_change=TestingState.set_new_test_date,
                                width="100%"
                            ),
                            rx.select(
                                ["Pass", "Fail", "Partial"],
                                value=TestingState.new_test_result,
                                on_change=TestingState.set_new_test_result,
                                width="100%"
                            ),
                            rx.input(
                                placeholder="Evidence File Name",
                                value=TestingState.new_test_evidence,
                                on_change=TestingState.set_new_test_evidence,
                                width="100%"
                            ),
                            rx.text_area(
                                placeholder="Test Notes",
                                value=TestingState.new_test_notes,
                                on_change=TestingState.set_new_test_notes,
                                width="100%"
                            ),
                            rx.hstack(
                                rx.button(
                                    "Record Test",
                                    on_click=TestingState.create_control_test,
                                    bg="#3b82f6",
                                    color="white",
                                    _hover={"bg": "#2563eb"}
                                ),
                                rx.button(
                                    "Cancel",
                                    on_click=TestingState.toggle_test_form,
                                    bg="#e2e8f0",
                                    color="#0f172a"
                                ),
                                spacing="3"
                            ),
                            spacing="4",
                            width="100%"
                        ),
                        bg="#f8fafc",
                        padding="20px",
                        border_radius="8px",
                        margin_bottom="20px"
                    ),
                    rx.fragment()
                ),
                
                # Test Records List
                rx.foreach(
                    TestingState.control_tests,
                    lambda test: rx.box(
                        rx.hstack(
                            rx.vstack(
                                rx.hstack(
                                    rx.badge(test["control_ccf_id"], color_scheme="blue", font_family="monospace"),
                                    rx.badge(
                                        test["result"],
                                        color_scheme=rx.cond(test["result"] == "Pass", "green", rx.cond(test["result"] == "Fail", "red", "yellow"))
                                    ),
                                    spacing="3"
                                ),
                                rx.text(test["notes"], font_size="14px", color="#64748b", margin_top="8px"),
                                rx.hstack(
                                    rx.text("Tested by: " + test["tester"].to_string(), font_size="13px", color="#64748b"),
                                    rx.text("Date: " + test["test_date"].to_string(), font_size="13px", color="#64748b"),
                                    rx.cond(
                                        test["evidence"] != "",
                                        rx.hstack(
                                            rx.icon("paperclip", size=14, color="#64748b"),
                                            rx.text(test["evidence"], font_size="13px", color="#64748b"),
                                            spacing="1"
                                        ),
                                        rx.fragment()
                                    ),
                                    spacing="5",
                                    margin_top="10px"
                                ),
                                align_items="start",
                                flex="1"
                            ),
                            width="100%"
                        ),
                        bg="white",
                        padding="20px",
                        border_radius="12px",
                        border=rx.cond(
                            test["result"] == "Pass",
                            "1px solid #86efac",
                            rx.cond(test["result"] == "Fail", "1px solid #fca5a5", "1px solid #fcd34d")
                        ),
                        margin_bottom="15px"
                    )
                ),
                
                bg="white",
                padding="30px",
                border_radius="12px",
                border="1px solid #e2e8f0"
            ),
            
            spacing="6",
            width="100%"
        )
    )


# Issues Page
@rx.page(route="/issues", title="Issues - GRC Platform", on_load=IssueState.load_all_data)
def issues() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Issue Management", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Track and manage issues identified during control testing", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            # Stats Cards
            rx.grid(
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.icon("triangle-alert", size=24, color="#ef4444"),
                            bg="#fef2f2",
                            padding="10px",
                            border_radius="50%"
                        ),
                        rx.vstack(
                            rx.text("Open Issues", font_size="14px", color="#64748b"),
                            rx.text(IssueState.open_issues, font_size="28px", font_weight="bold", color="#ef4444"),
                            spacing="0",
                            align_items="start"
                        ),
                        spacing="4"
                    ),
                    bg="white",
                    padding="20px",
                    border_radius="12px",
                    border="1px solid #e2e8f0"
                ),
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.icon("list-checks", size=24, color="#3b82f6"),
                            bg="#eff6ff",
                            padding="10px",
                            border_radius="50%"
                        ),
                        rx.vstack(
                            rx.text("Total Issues", font_size="14px", color="#64748b"),
                            rx.text(IssueState.total_issues, font_size="28px", font_weight="bold", color="#3b82f6"),
                            spacing="0",
                            align_items="start"
                        ),
                        spacing="4"
                    ),
                    bg="white",
                    padding="20px",
                    border_radius="12px",
                    border="1px solid #e2e8f0"
                ),
                columns="2",
                spacing="4",
                width="100%",
                max_width="500px",
                margin_bottom="30px"
            ),
            
            # Issues Section
            rx.box(
                rx.hstack(
                    rx.heading("All Issues", font_size="24px", font_weight="600"),
                    rx.button(
                        rx.icon("plus", size=20),
                        " Report Issue",
                        on_click=IssueState.toggle_issue_form,
                        bg="#ef4444",
                        color="white",
                        _hover={"bg": "#dc2626"},
                        padding="12px 20px",
                        border_radius="8px",
                        font_weight="600"
                    ),
                    justify="between",
                    width="100%",
                    margin_bottom="20px"
                ),
                
                # Create Form
                rx.cond(
                    IssueState.show_issue_form,
                    rx.box(
                        rx.vstack(
                            rx.input(
                                placeholder="Issue Title",
                                value=IssueState.new_issue_title,
                                on_change=IssueState.set_new_issue_title,
                                width="100%"
                            ),
                            rx.text_area(
                                placeholder="Description",
                                value=IssueState.new_issue_description,
                                on_change=IssueState.set_new_issue_description,
                                width="100%"
                            ),
                            rx.select(
                                ["Low", "Medium", "High", "Critical"],
                                value=IssueState.new_issue_severity,
                                on_change=IssueState.set_new_issue_severity,
                                width="100%"
                            ),
                            rx.input(
                                placeholder="Assigned To",
                                value=IssueState.new_issue_assigned_to,
                                on_change=IssueState.set_new_issue_assigned_to,
                                width="100%"
                            ),
                            rx.input(
                                placeholder="Due Date (YYYY-MM-DD)",
                                value=IssueState.new_issue_due_date,
                                on_change=IssueState.set_new_issue_due_date,
                                width="100%"
                            ),
                            rx.hstack(
                                rx.button(
                                    "Create Issue",
                                    on_click=IssueState.create_issue,
                                    bg="#ef4444",
                                    color="white",
                                    _hover={"bg": "#dc2626"}
                                ),
                                rx.button(
                                    "Cancel",
                                    on_click=IssueState.toggle_issue_form,
                                    bg="#e2e8f0",
                                    color="#0f172a"
                                ),
                                spacing="3"
                            ),
                            spacing="4",
                            width="100%"
                        ),
                        bg="#fef2f2",
                        padding="20px",
                        border_radius="8px",
                        margin_bottom="20px"
                    ),
                    rx.fragment()
                ),
                
                # Issues List
                rx.foreach(
                    IssueState.issues,
                    lambda issue: rx.box(
                        rx.hstack(
                            rx.vstack(
                                rx.hstack(
                                    rx.badge(
                                        issue["severity"],
                                        color_scheme=rx.cond(
                                            issue["severity"] == "Critical", "red",
                                            rx.cond(issue["severity"] == "High", "orange",
                                            rx.cond(issue["severity"] == "Medium", "yellow", "gray"))
                                        )
                                    ),
                                    rx.badge(
                                        issue["status"],
                                        color_scheme=rx.cond(
                                            issue["status"] == "Open", "red",
                                            rx.cond(issue["status"] == "In Progress", "yellow",
                                            rx.cond(issue["status"] == "Resolved", "green", "gray"))
                                        )
                                    ),
                                    spacing="3"
                                ),
                                rx.text(issue["title"], font_size="18px", font_weight="600", margin_top="8px"),
                                rx.text(issue["description"], font_size="14px", color="#64748b", margin_top="5px"),
                                rx.hstack(
                                    rx.text("Assigned: " + issue["assigned_to"].to_string(), font_size="13px", color="#64748b"),
                                    rx.text("Due: " + issue["due_date"].to_string(), font_size="13px", color="#64748b"),
                                    spacing="5",
                                    margin_top="10px"
                                ),
                                align_items="start",
                                flex="1"
                            ),
                            rx.vstack(
                                rx.cond(
                                    issue["status"] == "Open",
                                    rx.button(
                                        "Start",
                                        on_click=lambda: IssueState.update_issue_status(issue["id"], "In Progress"),
                                        bg="#f59e0b",
                                        color="white",
                                        size="2"
                                    ),
                                    rx.fragment()
                                ),
                                rx.cond(
                                    issue["status"] == "In Progress",
                                    rx.button(
                                        "Resolve",
                                        on_click=lambda: IssueState.update_issue_status(issue["id"], "Resolved"),
                                        bg="#10b981",
                                        color="white",
                                        size="2"
                                    ),
                                    rx.fragment()
                                ),
                                spacing="2"
                            ),
                            width="100%",
                            align_items="start"
                        ),
                        bg="white",
                        padding="20px",
                        border_radius="12px",
                        border=rx.cond(
                            issue["status"] == "Open",
                            "2px solid #ef4444",
                            rx.cond(issue["status"] == "In Progress", "2px solid #f59e0b", "1px solid #e2e8f0")
                        ),
                        margin_bottom="15px"
                    )
                ),
                
                bg="white",
                padding="30px",
                border_radius="12px",
                border="1px solid #e2e8f0"
            ),
            
            spacing="6",
            width="100%"
        )
    )


# KRI Page
@rx.page(route="/kris", title="KRIs - GRC Platform", on_load=KRIState.load_all_data)
def kris() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Key Risk Indicators (KRIs)", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Monitor metrics that indicate changes in risk levels", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            # KRI Section
            rx.box(
                rx.hstack(
                    rx.heading("Risk Indicators", font_size="24px", font_weight="600"),
                    rx.button(
                        rx.icon("plus", size=20),
                        " Add KRI",
                        on_click=KRIState.toggle_kri_form,
                        bg="#3b82f6",
                        color="white",
                        _hover={"bg": "#2563eb"},
                        padding="12px 20px",
                        border_radius="8px",
                        font_weight="600"
                    ),
                    justify="between",
                    width="100%",
                    margin_bottom="20px"
                ),
                
                # Create Form
                rx.cond(
                    KRIState.show_kri_form,
                    rx.box(
                        rx.vstack(
                            rx.input(
                                placeholder="KRI Name",
                                value=KRIState.new_kri_name,
                                on_change=KRIState.set_new_kri_name,
                                width="100%"
                            ),
                            rx.text_area(
                                placeholder="Description",
                                value=KRIState.new_kri_description,
                                on_change=KRIState.set_new_kri_description,
                                width="100%"
                            ),
                            rx.input(
                                placeholder="Risk ID (e.g., risk-001)",
                                value=KRIState.new_kri_risk_id,
                                on_change=KRIState.set_new_kri_risk_id,
                                width="100%"
                            ),
                            rx.hstack(
                                rx.input(placeholder="Green Threshold", value=KRIState.new_kri_threshold_green.to_string(), on_change=KRIState.set_new_kri_threshold_green, width="30%"),
                                rx.input(placeholder="Yellow Threshold", value=KRIState.new_kri_threshold_yellow.to_string(), on_change=KRIState.set_new_kri_threshold_yellow, width="30%"),
                                rx.input(placeholder="Red Threshold", value=KRIState.new_kri_threshold_red.to_string(), on_change=KRIState.set_new_kri_threshold_red, width="30%"),
                                spacing="3",
                                width="100%"
                            ),
                            rx.hstack(
                                rx.input(placeholder="Current Value", value=KRIState.new_kri_current_value.to_string(), on_change=KRIState.set_new_kri_current_value, width="50%"),
                                rx.select(["Count", "Percentage", "Minutes", "Days", "Currency"], value=KRIState.new_kri_unit, on_change=KRIState.set_new_kri_unit, width="50%"),
                                spacing="3",
                                width="100%"
                            ),
                            rx.hstack(
                                rx.select(["Weekly", "Monthly", "Quarterly", "Annually"], value=KRIState.new_kri_frequency, on_change=KRIState.set_new_kri_frequency, width="50%"),
                                rx.input(placeholder="Owner", value=KRIState.new_kri_owner, on_change=KRIState.set_new_kri_owner, width="50%"),
                                spacing="3",
                                width="100%"
                            ),
                            rx.hstack(
                                rx.button("Create KRI", on_click=KRIState.create_kri, bg="#3b82f6", color="white"),
                                rx.button("Cancel", on_click=KRIState.toggle_kri_form, bg="#e2e8f0"),
                                spacing="3"
                            ),
                            spacing="4",
                            width="100%"
                        ),
                        bg="#f8fafc",
                        padding="20px",
                        border_radius="8px",
                        margin_bottom="20px"
                    ),
                    rx.fragment()
                ),
                
                # KRIs List
                rx.foreach(
                    KRIState.kris,
                    lambda kri: rx.box(
                        rx.hstack(
                            rx.vstack(
                                rx.text(kri["name"], font_size="18px", font_weight="600"),
                                rx.text(kri["description"], font_size="14px", color="#64748b", margin_top="5px"),
                                rx.hstack(
                                    rx.text("Frequency: " + kri["frequency"].to_string(), font_size="13px", color="#64748b"),
                                    rx.text("Owner: " + kri["owner"].to_string(), font_size="13px", color="#64748b"),
                                    spacing="5",
                                    margin_top="10px"
                                ),
                                align_items="start",
                                flex="1"
                            ),
                            rx.vstack(
                                rx.text("Current Value", font_size="12px", color="#64748b"),
                                rx.hstack(
                                    rx.text(kri["current_value"], font_size="32px", font_weight="bold", 
                                           color=rx.cond(
                                               kri["current_value"] <= kri["threshold_green"], "#10b981",
                                               rx.cond(kri["current_value"] <= kri["threshold_yellow"], "#f59e0b", "#ef4444")
                                           )),
                                    rx.text(kri["unit"], font_size="14px", color="#64748b", margin_left="5px"),
                                    align_items="baseline"
                                ),
                                rx.hstack(
                                    rx.box(bg="#10b981", width="12px", height="12px", border_radius="2px"),
                                    rx.text("<=" + kri["threshold_green"].to_string(), font_size="11px", color="#64748b"),
                                    rx.box(bg="#f59e0b", width="12px", height="12px", border_radius="2px"),
                                    rx.text("<=" + kri["threshold_yellow"].to_string(), font_size="11px", color="#64748b"),
                                    rx.box(bg="#ef4444", width="12px", height="12px", border_radius="2px"),
                                    rx.text(">" + kri["threshold_yellow"].to_string(), font_size="11px", color="#64748b"),
                                    spacing="2",
                                    margin_top="10px"
                                ),
                                align_items="end",
                                spacing="2"
                            ),
                            width="100%",
                            align_items="start"
                        ),
                        bg="white",
                        padding="20px",
                        border_radius="12px",
                        border="1px solid #e2e8f0",
                        margin_bottom="15px"
                    )
                ),
                
                bg="white",
                padding="30px",
                border_radius="12px",
                border="1px solid #e2e8f0"
            ),
            
            spacing="6",
            width="100%"
        )
    )


# KCI Page
@rx.page(route="/kcis", title="KCIs - GRC Platform", on_load=KCIState.load_all_data)
def kcis() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Key Control Indicators (KCIs)", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Monitor control effectiveness and operational metrics", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            # KCI Section
            rx.box(
                rx.hstack(
                    rx.heading("Control Indicators", font_size="24px", font_weight="600"),
                    rx.button(
                        rx.icon("plus", size=20),
                        " Add KCI",
                        on_click=KCIState.toggle_kci_form,
                        bg="#8b5cf6",
                        color="white",
                        _hover={"bg": "#7c3aed"},
                        padding="12px 20px",
                        border_radius="8px",
                        font_weight="600"
                    ),
                    justify="between",
                    width="100%",
                    margin_bottom="20px"
                ),
                
                # Create Form
                rx.cond(
                    KCIState.show_kci_form,
                    rx.box(
                        rx.vstack(
                            rx.input(
                                placeholder="KCI Name",
                                value=KCIState.new_kci_name,
                                on_change=KCIState.set_new_kci_name,
                                width="100%"
                            ),
                            rx.text_area(
                                placeholder="Description",
                                value=KCIState.new_kci_description,
                                on_change=KCIState.set_new_kci_description,
                                width="100%"
                            ),
                            rx.select(
                                KCIState.kris.to(list).map(lambda k: k["id"] + " - " + k["name"]),
                                placeholder="Link to KRI",
                                on_change=KCIState.set_new_kci_kri_id,
                                width="100%"
                            ),
                            rx.hstack(
                                rx.input(placeholder="Green Threshold", value=KCIState.new_kci_threshold_green.to_string(), on_change=KCIState.set_new_kci_threshold_green, width="30%"),
                                rx.input(placeholder="Yellow Threshold", value=KCIState.new_kci_threshold_yellow.to_string(), on_change=KCIState.set_new_kci_threshold_yellow, width="30%"),
                                rx.input(placeholder="Red Threshold", value=KCIState.new_kci_threshold_red.to_string(), on_change=KCIState.set_new_kci_threshold_red, width="30%"),
                                spacing="3",
                                width="100%"
                            ),
                            rx.hstack(
                                rx.input(placeholder="Current Value", value=KCIState.new_kci_current_value.to_string(), on_change=KCIState.set_new_kci_current_value, width="50%"),
                                rx.select(["Percentage", "Count", "Minutes", "Days"], value=KCIState.new_kci_unit, on_change=KCIState.set_new_kci_unit, width="50%"),
                                spacing="3",
                                width="100%"
                            ),
                            rx.hstack(
                                rx.select(["Weekly", "Monthly", "Quarterly", "Annually"], value=KCIState.new_kci_frequency, on_change=KCIState.set_new_kci_frequency, width="50%"),
                                rx.input(placeholder="Owner", value=KCIState.new_kci_owner, on_change=KCIState.set_new_kci_owner, width="50%"),
                                spacing="3",
                                width="100%"
                            ),
                            rx.hstack(
                                rx.button("Create KCI", on_click=KCIState.create_kci, bg="#8b5cf6", color="white"),
                                rx.button("Cancel", on_click=KCIState.toggle_kci_form, bg="#e2e8f0"),
                                spacing="3"
                            ),
                            spacing="4",
                            width="100%"
                        ),
                        bg="#faf5ff",
                        padding="20px",
                        border_radius="8px",
                        margin_bottom="20px"
                    ),
                    rx.fragment()
                ),
                
                # KCIs List
                rx.foreach(
                    KCIState.kcis,
                    lambda kci: rx.box(
                        rx.hstack(
                            rx.vstack(
                                rx.text(kci["name"], font_size="18px", font_weight="600"),
                                rx.text(kci["description"], font_size="14px", color="#64748b", margin_top="5px"),
                                rx.hstack(
                                    rx.text("Frequency: " + kci["frequency"].to_string(), font_size="13px", color="#64748b"),
                                    rx.text("Owner: " + kci["owner"].to_string(), font_size="13px", color="#64748b"),
                                    spacing="5",
                                    margin_top="10px"
                                ),
                                align_items="start",
                                flex="1"
                            ),
                            rx.vstack(
                                rx.text("Current Value", font_size="12px", color="#64748b"),
                                rx.hstack(
                                    rx.text(kci["current_value"], font_size="32px", font_weight="bold", 
                                           color=rx.cond(
                                               kci["current_value"] >= kci["threshold_green"], "#10b981",
                                               rx.cond(kci["current_value"] >= kci["threshold_yellow"], "#f59e0b", "#ef4444")
                                           )),
                                    rx.text(kci["unit"], font_size="14px", color="#64748b", margin_left="5px"),
                                    align_items="baseline"
                                ),
                                rx.hstack(
                                    rx.box(bg="#10b981", width="12px", height="12px", border_radius="2px"),
                                    rx.text(">=" + kci["threshold_green"].to_string(), font_size="11px", color="#64748b"),
                                    rx.box(bg="#f59e0b", width="12px", height="12px", border_radius="2px"),
                                    rx.text(">=" + kci["threshold_yellow"].to_string(), font_size="11px", color="#64748b"),
                                    rx.box(bg="#ef4444", width="12px", height="12px", border_radius="2px"),
                                    rx.text("<" + kci["threshold_yellow"].to_string(), font_size="11px", color="#64748b"),
                                    spacing="2",
                                    margin_top="10px"
                                ),
                                align_items="end",
                                spacing="2"
                            ),
                            width="100%",
                            align_items="start"
                        ),
                        bg="white",
                        padding="20px",
                        border_radius="12px",
                        border="1px solid #e2e8f0",
                        margin_bottom="15px"
                    )
                ),
                
                bg="white",
                padding="30px",
                border_radius="12px",
                border="1px solid #e2e8f0"
            ),
            
            spacing="6",
            width="100%"
        )
    )


# Risk Heatmap Page - Both Matrix and Network Graph
@rx.page(route="/heatmap", title="Risk Heatmap - GRC Platform", on_load=HeatmapState.load_all_data)
def heatmap() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Risk Heatmap & Visualization", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Visual representation of risk landscape and relationships", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            # Risk Matrix Heatmap
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.icon("grid-3x3", size=24, color="#ef4444"),
                        rx.text("Risk Matrix (Impact vs Likelihood)", font_size="20px", font_weight="600"),
                        spacing="3"
                    ),
                    rx.text("Position indicates risk severity - top-right is highest risk", font_size="14px", color="#64748b", margin_bottom="20px"),
                    
                    # Matrix Grid
                    rx.box(
                        # Y-axis label
                        rx.box(
                            rx.text("IMPACT", font_size="12px", font_weight="600", color="#64748b", 
                                   style={"writing_mode": "vertical-rl", "transform": "rotate(180deg)"}),
                            position="absolute",
                            left="-30px",
                            top="50%",
                            transform="translateY(-50%)"
                        ),
                        # Grid
                        rx.grid(
                            # Row 5 (High Impact)
                            rx.box(bg="#fef3c7", border="1px solid #fcd34d", height="60px", border_radius="4px", display="flex", align_items="center", justify_content="center",
                                  _hover={"bg": "#fde68a"}),
                            rx.box(bg="#fed7aa", border="1px solid #fdba74", height="60px", border_radius="4px",
                                  _hover={"bg": "#fdba74"}),
                            rx.box(bg="#fecaca", border="1px solid #fca5a5", height="60px", border_radius="4px",
                                  _hover={"bg": "#fca5a5"}),
                            rx.box(bg="#fecaca", border="1px solid #f87171", height="60px", border_radius="4px",
                                  _hover={"bg": "#f87171"}),
                            rx.box(bg="#fee2e2", border="1px solid #ef4444", height="60px", border_radius="4px", 
                                  _hover={"bg": "#ef4444"}),
                            # Row 4
                            rx.box(bg="#dcfce7", border="1px solid #86efac", height="60px", border_radius="4px",
                                  _hover={"bg": "#86efac"}),
                            rx.box(bg="#fef3c7", border="1px solid #fcd34d", height="60px", border_radius="4px",
                                  _hover={"bg": "#fde68a"}),
                            rx.box(bg="#fed7aa", border="1px solid #fdba74", height="60px", border_radius="4px",
                                  _hover={"bg": "#fdba74"}),
                            rx.box(bg="#fecaca", border="1px solid #fca5a5", height="60px", border_radius="4px",
                                  _hover={"bg": "#fca5a5"}),
                            rx.box(bg="#fecaca", border="1px solid #f87171", height="60px", border_radius="4px",
                                  _hover={"bg": "#f87171"}),
                            # Row 3 (Medium Impact)
                            rx.box(bg="#dcfce7", border="1px solid #86efac", height="60px", border_radius="4px",
                                  _hover={"bg": "#86efac"}),
                            rx.box(bg="#dcfce7", border="1px solid #4ade80", height="60px", border_radius="4px",
                                  _hover={"bg": "#4ade80"}),
                            rx.box(bg="#fef3c7", border="1px solid #fcd34d", height="60px", border_radius="4px",
                                  _hover={"bg": "#fde68a"}),
                            rx.box(bg="#fed7aa", border="1px solid #fdba74", height="60px", border_radius="4px",
                                  _hover={"bg": "#fdba74"}),
                            rx.box(bg="#fecaca", border="1px solid #fca5a5", height="60px", border_radius="4px",
                                  _hover={"bg": "#fca5a5"}),
                            # Row 2
                            rx.box(bg="#d1fae5", border="1px solid #6ee7b7", height="60px", border_radius="4px",
                                  _hover={"bg": "#6ee7b7"}),
                            rx.box(bg="#dcfce7", border="1px solid #86efac", height="60px", border_radius="4px",
                                  _hover={"bg": "#86efac"}),
                            rx.box(bg="#dcfce7", border="1px solid #4ade80", height="60px", border_radius="4px",
                                  _hover={"bg": "#4ade80"}),
                            rx.box(bg="#fef3c7", border="1px solid #fcd34d", height="60px", border_radius="4px",
                                  _hover={"bg": "#fde68a"}),
                            rx.box(bg="#fed7aa", border="1px solid #fdba74", height="60px", border_radius="4px",
                                  _hover={"bg": "#fdba74"}),
                            # Row 1 (Low Impact)
                            rx.box(bg="#d1fae5", border="1px solid #6ee7b7", height="60px", border_radius="4px",
                                  _hover={"bg": "#6ee7b7"}),
                            rx.box(bg="#d1fae5", border="1px solid #6ee7b7", height="60px", border_radius="4px",
                                  _hover={"bg": "#6ee7b7"}),
                            rx.box(bg="#dcfce7", border="1px solid #86efac", height="60px", border_radius="4px",
                                  _hover={"bg": "#86efac"}),
                            rx.box(bg="#dcfce7", border="1px solid #4ade80", height="60px", border_radius="4px",
                                  _hover={"bg": "#4ade80"}),
                            rx.box(bg="#fef3c7", border="1px solid #fcd34d", height="60px", border_radius="4px",
                                  _hover={"bg": "#fde68a"}),
                            columns="5",
                            spacing="2",
                            width="400px"
                        ),
                        # X-axis label
                        rx.text("LIKELIHOOD", font_size="12px", font_weight="600", color="#64748b", text_align="center", margin_top="10px"),
                        position="relative",
                        padding_left="40px"
                    ),
                    
                    # Legend
                    rx.hstack(
                        rx.hstack(rx.box(bg="#d1fae5", width="20px", height="20px", border_radius="4px"), rx.text("Low", font_size="13px"), spacing="2"),
                        rx.hstack(rx.box(bg="#fef3c7", width="20px", height="20px", border_radius="4px"), rx.text("Medium", font_size="13px"), spacing="2"),
                        rx.hstack(rx.box(bg="#fed7aa", width="20px", height="20px", border_radius="4px"), rx.text("High", font_size="13px"), spacing="2"),
                        rx.hstack(rx.box(bg="#fecaca", width="20px", height="20px", border_radius="4px"), rx.text("Critical", font_size="13px"), spacing="2"),
                        spacing="6",
                        margin_top="20px"
                    ),
                    
                    align_items="start",
                    spacing="4"
                ),
                bg="white",
                padding="30px",
                border_radius="12px",
                border="1px solid #e2e8f0",
                margin_bottom="30px"
            ),
            
            # Risk Network Graph
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.icon("git-branch", size=24, color="#8b5cf6"),
                        rx.text("Risk Relationship Network", font_size="20px", font_weight="600"),
                        spacing="3"
                    ),
                    rx.text("Visual flow: Risks → KRIs → KCIs → Controls", font_size="14px", color="#64748b", margin_bottom="20px"),
                    
                    # Network Visualization
                    rx.foreach(
                        HeatmapState.risks,
                        lambda risk: rx.box(
                            rx.vstack(
                                # Risk Node
                                rx.box(
                                    rx.hstack(
                                        rx.icon("alert-triangle", size=20, color="white"),
                                        rx.text(risk["name"], font_size="14px", font_weight="600", color="white"),
                                        spacing="2"
                                    ),
                                    bg=rx.cond(
                                        risk["residual_risk_score"] >= 7, "#ef4444",
                                        rx.cond(risk["residual_risk_score"] >= 4, "#f59e0b", "#10b981")
                                    ),
                                    padding="12px 20px",
                                    border_radius="8px",
                                    box_shadow="md"
                                ),
                                
                                # Connector Line
                                rx.box(
                                    width="2px",
                                    height="30px",
                                    bg="#e2e8f0"
                                ),
                                
                                # KRIs linked to this risk
                                rx.hstack(
                                    rx.foreach(
                                        HeatmapState.kris.to(list).filter(lambda k: k["risk_id"] == risk["id"]),
                                        lambda kri: rx.vstack(
                                            rx.box(
                                                rx.text(kri["name"], font_size="12px", font_weight="500", color="#1e40af"),
                                                bg="#eff6ff",
                                                padding="8px 14px",
                                                border_radius="6px",
                                                border="1px solid #bfdbfe"
                                            ),
                                            rx.box(width="2px", height="20px", bg="#e2e8f0"),
                                            # KCIs linked to this KRI
                                            rx.hstack(
                                                rx.foreach(
                                                    HeatmapState.kcis.to(list).filter(lambda c: c["kri_id"] == kri["id"]),
                                                    lambda kci: rx.box(
                                                        rx.text(kci["name"], font_size="11px", color="#6b21a8"),
                                                        bg="#faf5ff",
                                                        padding="6px 10px",
                                                        border_radius="4px",
                                                        border="1px solid #e9d5ff"
                                                    )
                                                ),
                                                spacing="2",
                                                flex_wrap="wrap"
                                            ),
                                            align_items="center",
                                            spacing="2"
                                        )
                                    ),
                                    spacing="4",
                                    flex_wrap="wrap",
                                    justify="center"
                                ),
                                
                                align_items="center",
                                spacing="2",
                                padding="20px",
                                width="100%"
                            ),
                            bg="#fafafa",
                            border_radius="12px",
                            border="1px solid #e2e8f0",
                            margin_bottom="20px"
                        )
                    ),
                    
                    align_items="start",
                    spacing="4",
                    width="100%"
                ),
                bg="white",
                padding="30px",
                border_radius="12px",
                border="1px solid #e2e8f0"
            ),
            
            # Summary Stats
            rx.grid(
                rx.box(
                    rx.vstack(
                        rx.text("Total Risks", font_size="14px", color="#64748b"),
                        rx.text(HeatmapState.total_risks, font_size="36px", font_weight="bold", color="#ef4444"),
                        spacing="2"
                    ),
                    bg="white",
                    padding="20px",
                    border_radius="12px",
                    border="1px solid #e2e8f0",
                    text_align="center"
                ),
                rx.box(
                    rx.vstack(
                        rx.text("Avg Risk Score", font_size="14px", color="#64748b"),
                        rx.text(HeatmapState.avg_residual_risk, font_size="36px", font_weight="bold", color="#f59e0b"),
                        spacing="2"
                    ),
                    bg="white",
                    padding="20px",
                    border_radius="12px",
                    border="1px solid #e2e8f0",
                    text_align="center"
                ),
                rx.box(
                    rx.vstack(
                        rx.text("Control Effectiveness", font_size="14px", color="#64748b"),
                        rx.text(HeatmapState.control_effectiveness.to_string() + "%", font_size="36px", font_weight="bold", color="#10b981"),
                        spacing="2"
                    ),
                    bg="white",
                    padding="20px",
                    border_radius="12px",
                    border="1px solid #e2e8f0",
                    text_align="center"
                ),
                columns="3",
                spacing="4",
                width="100%",
                margin_top="30px"
            ),
            
            spacing="6",
            width="100%"
        )
    )


# Create main app
app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="blue",
    )
)
