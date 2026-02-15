"""Main GRC Platform Application - Pure Python with Reflex"""
import reflex as rx
from typing import Dict
from .state import GRCState, FrameworkState, ControlState, PolicyState, RiskState

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
                        rx.icon("alert-triangle", size=20),
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
                    rx.text(GRCState.stats["enabled_frameworks"], font_size="36px", font_weight="bold", color="#0f172a"),
                    rx.text(f"{len(GRCState.unified_controls)} unified controls", font_size="12px", color="#64748b", margin_top="5px"),
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
                            rx.icon("check-circle-2", size=24, color="#10b981"),
                            bg="#f0fdf4",
                            padding="10px",
                            border_radius="50%"
                        ),
                        justify="between",
                        width="100%",
                        margin_bottom="15px"
                    ),
                    rx.text("Control Effectiveness", font_size="14px", color="#64748b", margin_bottom="5px"),
                    rx.text(f"{GRCState.stats['control_effectiveness']}%", font_size="36px", font_weight="bold", color="#0f172a"),
                    rx.text(f"{GRCState.stats['passed_tests']} of {GRCState.stats.get('total_tests', 0)} passed", font_size="12px", color="#10b981", margin_top="5px"),
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
                            rx.icon("alert-triangle", size=24, color="#ef4444"),
                            bg="#fef2f2",
                            padding="10px",
                            border_radius="50%"
                        ),
                        justify="between",
                        width="100%",
                        margin_bottom="15px"
                    ),
                    rx.text("Open Issues", font_size="14px", color="#64748b", margin_bottom="5px"),
                    rx.text(GRCState.stats["open_issues"], font_size="36px", font_weight="bold", color="#0f172a"),
                    rx.text(f"{GRCState.stats['total_issues']} total issues", font_size="12px", color="#64748b", margin_top="5px"),
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
                    rx.text(f"{GRCState.stats['avg_residual_risk']:.1f}", font_size="36px", font_weight="bold", color="#0f172a"),
                    rx.text(f"{GRCState.stats['total_risks']} risks tracked", font_size="12px", color="#64748b", margin_top="5px"),
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
                                            rx.text(f"Version {fw['version']}", font_size="14px", color="#64748b"),
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
                                    rx.text(f"{fw['total_controls']} controls", font_size="14px", color="#64748b", font_weight="600", margin_top="10px"),
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

# Helper function to render mapping details for a control
def render_mapping_details(ctrl: Dict) -> rx.Component:
    """Render the expandable mapping details for a control"""
    return rx.box(
        # Mapping Flow Visualization
        rx.vstack(
            # Header
            rx.hstack(
                rx.icon("git-branch", size=18, color="#8b5cf6"),
                rx.text("Mapping Details", font_size="16px", font_weight="600", color="#0f172a"),
                spacing="2"
            ),
            
            # Visual Flow Diagram
            rx.box(
                rx.hstack(
                    # Framework Controls Section
                    rx.vstack(
                        rx.hstack(
                            rx.icon("shield", size=16, color="#3b82f6"),
                            rx.text("Framework Controls", font_size="12px", font_weight="600", color="#3b82f6"),
                            spacing="1"
                        ),
                        rx.cond(
                            ctrl["mapped_framework_controls"].length() > 0,
                            rx.vstack(
                                rx.foreach(
                                    ctrl["mapped_framework_controls"],
                                    lambda fc: rx.box(
                                        rx.vstack(
                                            rx.text(fc["framework"], font_size="10px", color="#64748b", font_weight="600"),
                                            rx.text(fc["control_id"], font_size="13px", font_weight="600", color="#0f172a"),
                                            rx.text(fc["control_name"], font_size="11px", color="#64748b"),
                                            spacing="0",
                                            align_items="start"
                                        ),
                                        bg="#eff6ff",
                                        padding="10px",
                                        border_radius="8px",
                                        border="1px solid #bfdbfe",
                                        width="100%"
                                    )
                                ),
                                spacing="2",
                                width="100%"
                            ),
                            rx.box(
                                rx.text("No framework controls mapped yet", font_size="12px", color="#94a3b8", font_style="italic"),
                                bg="#f8fafc",
                                padding="15px",
                                border_radius="8px",
                                border="1px dashed #e2e8f0",
                                text_align="center"
                            )
                        ),
                        bg="white",
                        padding="15px",
                        border_radius="12px",
                        border="1px solid #e2e8f0",
                        min_width="220px",
                        align_items="start"
                    ),
                    
                    # Arrow 1
                    rx.vstack(
                        rx.icon("arrow-right", size=24, color="#10b981"),
                        rx.text("maps to", font_size="10px", color="#64748b"),
                        spacing="1",
                        align_items="center",
                        padding_x="10px"
                    ),
                    
                    # Unified Control (Center)
                    rx.vstack(
                        rx.hstack(
                            rx.icon("target", size=16, color="#10b981"),
                            rx.text("Unified Control (CCF)", font_size="12px", font_weight="600", color="#10b981"),
                            spacing="1"
                        ),
                        rx.box(
                            rx.vstack(
                                rx.badge(ctrl["ccf_id"], color_scheme="green", font_family="monospace"),
                                rx.text(ctrl["name"], font_size="13px", font_weight="600", color="#0f172a", text_align="center"),
                                rx.text(f"Type: {ctrl['control_type']}", font_size="11px", color="#64748b"),
                                spacing="2",
                                align_items="center"
                            ),
                            bg="#f0fdf4",
                            padding="15px",
                            border_radius="8px",
                            border="2px solid #86efac",
                            width="100%"
                        ),
                        bg="white",
                        padding="15px",
                        border_radius="12px",
                        border="2px solid #10b981",
                        min_width="200px",
                        align_items="center"
                    ),
                    
                    # Arrow 2
                    rx.vstack(
                        rx.icon("arrow-right", size=24, color="#8b5cf6"),
                        rx.text("implements", font_size="10px", color="#64748b"),
                        spacing="1",
                        align_items="center",
                        padding_x="10px"
                    ),
                    
                    # Policies Section
                    rx.vstack(
                        rx.hstack(
                            rx.icon("file-text", size=16, color="#8b5cf6"),
                            rx.text("Internal Policies", font_size="12px", font_weight="600", color="#8b5cf6"),
                            spacing="1"
                        ),
                        rx.cond(
                            ctrl["mapped_policies"].length() > 0,
                            rx.vstack(
                                rx.foreach(
                                    ctrl["mapped_policies"],
                                    lambda pol: rx.box(
                                        rx.vstack(
                                            rx.text(pol["policy_id"], font_size="13px", font_weight="600", color="#0f172a"),
                                            rx.text(pol["policy_name"], font_size="11px", color="#64748b"),
                                            spacing="0",
                                            align_items="start"
                                        ),
                                        bg="#faf5ff",
                                        padding="10px",
                                        border_radius="8px",
                                        border="1px solid #e9d5ff",
                                        width="100%"
                                    )
                                ),
                                spacing="2",
                                width="100%"
                            ),
                            rx.box(
                                rx.text("No policies mapped yet", font_size="12px", color="#94a3b8", font_style="italic"),
                                bg="#f8fafc",
                                padding="15px",
                                border_radius="8px",
                                border="1px dashed #e2e8f0",
                                text_align="center"
                            )
                        ),
                        bg="white",
                        padding="15px",
                        border_radius="12px",
                        border="1px solid #e2e8f0",
                        min_width="220px",
                        align_items="start"
                    ),
                    
                    spacing="2",
                    align_items="center",
                    justify="center",
                    width="100%",
                    overflow_x="auto",
                    padding="10px"
                ),
                bg="#fafafa",
                padding="15px",
                border_radius="12px",
                margin_top="15px"
            ),
            
            # Summary Stats
            rx.hstack(
                rx.box(
                    rx.hstack(
                        rx.icon("layers", size=16, color="#3b82f6"),
                        rx.text(f"{ctrl['mapped_framework_controls'].length()} Framework Controls", font_size="13px", color="#64748b"),
                        spacing="2"
                    ),
                    bg="#eff6ff",
                    padding="8px 12px",
                    border_radius="6px"
                ),
                rx.box(
                    rx.hstack(
                        rx.icon("file-check", size=16, color="#8b5cf6"),
                        rx.text(f"{ctrl['mapped_policies'].length()} Policies", font_size="13px", color="#64748b"),
                        spacing="2"
                    ),
                    bg="#faf5ff",
                    padding="8px 12px",
                    border_radius="6px"
                ),
                rx.cond(
                    ctrl["automation_possible"],
                    rx.box(
                        rx.hstack(
                            rx.icon("zap", size=16, color="#f59e0b"),
                            rx.text("Automation Ready", font_size="13px", color="#64748b"),
                            spacing="2"
                        ),
                        bg="#fffbeb",
                        padding="8px 12px",
                        border_radius="6px"
                    ),
                    rx.fragment()
                ),
                spacing="3",
                margin_top="15px",
                flex_wrap="wrap"
            ),
            
            spacing="3",
            width="100%",
            align_items="start"
        ),
        bg="#f8fafc",
        padding="20px",
        border_radius="12px",
        border="1px solid #e2e8f0",
        margin_top="15px",
        width="100%"
    )

# Control Mapping Page
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
            
            # Create Control Button
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
                                        rx.text(f"Type: {ctrl['control_type']}", font_size="13px", color="#64748b"),
                                        rx.text(f"Frequency: {ctrl['frequency']}", font_size="13px", color="#64748b"),
                                        rx.text(f"Owner: {ctrl['owner']}", font_size="13px", color="#64748b"),
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
                            
                            # Expandable Mapping Details
                            rx.cond(
                                ControlState.expanded_controls.contains(ctrl["id"]),
                                render_mapping_details(ctrl),
                                rx.fragment()
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
                            rx.text(f"Category: {pol['category']} | Owner: {pol['owner']}", font_size="13px", color="#64748b", margin_top="8px"),
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
                                    rx.text(f"{risk['inherent_risk_score']:.1f}", font_size="20px", font_weight="bold", color="#ef4444"),
                                    spacing="0"
                                ),
                                rx.vstack(
                                    rx.text("Residual Risk", font_size="12px", color="#64748b"),
                                    rx.text(f"{risk['residual_risk_score']:.1f}", font_size="20px", font_weight="bold", color="#10b981"),
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

# Create main app
app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="blue",
    )
)
