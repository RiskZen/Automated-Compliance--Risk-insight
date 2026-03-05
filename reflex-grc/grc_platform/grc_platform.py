"""Main GRC Platform Application - Pure Python with Reflex"""
import reflex as rx
from typing import Dict, Any
from .state import (
    GRCState, FrameworkState, ControlState, PolicyState, RiskState,
    TestingState, IssueState, KRIState, KCIState, HeatmapState,
    AuthState, AIGovernanceState, AuditLogState, ConnectorState,
    GapAnalysisState, AuditManagementState
)


# Login Page
@rx.page(route="/login", title="Login - GRC Platform")
def login() -> rx.Component:
    return rx.center(
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.icon("shield-check", size=40, color="#3b82f6"),
                    rx.vstack(
                        rx.text("GRC Platform", font_size="28px", font_weight="bold", color="#0f172a"),
                        rx.text("Governance, Risk & Compliance", font_size="14px", color="#64748b"),
                        spacing="0",
                        align_items="start"
                    ),
                    spacing="3",
                    margin_bottom="30px"
                ),
                
                rx.text("Sign In", font_size="24px", font_weight="600", color="#0f172a", margin_bottom="20px"),
                
                rx.cond(
                    AuthState.login_error != "",
                    rx.box(
                        rx.text(AuthState.login_error, color="white", font_size="14px"),
                        bg="#ef4444",
                        padding="12px 20px",
                        border_radius="8px",
                        width="100%",
                        margin_bottom="15px"
                    ),
                    rx.fragment()
                ),
                
                rx.input(
                    placeholder="Email address",
                    value=AuthState.login_email,
                    on_change=AuthState.set_login_email,
                    width="100%",
                    height="48px",
                    border_radius="8px",
                    margin_bottom="15px"
                ),
                rx.input(
                    placeholder="Password",
                    type="password",
                    value=AuthState.login_password,
                    on_change=AuthState.set_login_password,
                    width="100%",
                    height="48px",
                    border_radius="8px",
                    margin_bottom="20px"
                ),
                rx.button(
                    "Sign In",
                    on_click=AuthState.login,
                    width="100%",
                    height="48px",
                    bg="#3b82f6",
                    color="white",
                    font_weight="600",
                    border_radius="8px",
                    _hover={"bg": "#2563eb"},
                    cursor="pointer"
                ),
                
                rx.text("Demo Credentials:", font_size="13px", color="#64748b", margin_top="30px", font_weight="600"),
                rx.vstack(
                    rx.text("admin@grcplatform.com / admin123", font_size="12px", color="#94a3b8"),
                    rx.text("auditor@grcplatform.com / auditor123", font_size="12px", color="#94a3b8"),
                    spacing="1",
                    align_items="center"
                ),
                
                spacing="0",
                width="100%"
            ),
            bg="white",
            padding="40px",
            border_radius="16px",
            box_shadow="0 25px 50px -12px rgba(0, 0, 0, 0.25)",
            width="400px"
        ),
        min_height="100vh",
        bg="linear-gradient(135deg, #1e3a5f 0%, #0f172a 100%)"
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
                        rx.icon("scan-search", size=20),
                        rx.text("Gap Analysis", font_size="14px", font_weight="500"),
                        rx.badge("AI", color_scheme="amber", size="1", variant="solid"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/gap-analysis",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
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
                        rx.icon("clipboard-list", size=20),
                        rx.text("Audit Planning", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/audit-planning",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                rx.link(
                    rx.hstack(
                        rx.icon("shield-check", size=20),
                        rx.text("Audit Readiness", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/audit-readiness",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
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
                
                rx.text("AI GOVERNANCE", font_size="11px", color="#64748b", font_weight="600", padding_left="15px", margin_top="20px"),
                rx.link(
                    rx.hstack(
                        rx.icon("brain", size=20),
                        rx.text("AI Models", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/ai-models",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                rx.link(
                    rx.hstack(
                        rx.icon("clipboard-list", size=20),
                        rx.text("AI Assessments", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/ai-assessments",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                
                rx.text("SYSTEM", font_size="11px", color="#64748b", font_weight="600", padding_left="15px", margin_top="20px"),
                rx.link(
                    rx.hstack(
                        rx.icon("plug", size=20),
                        rx.text("Connectors", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/connectors",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                rx.link(
                    rx.hstack(
                        rx.icon("scroll-text", size=20),
                        rx.text("Audit Logs", font_size="14px", font_weight="500"),
                        padding="12px 15px",
                        border_radius="8px",
                        _hover={"bg": "#1e293b"},
                        width="100%"
                    ),
                    href="/audit-logs",
                    style={"text_decoration": "none", "color": "#cbd5e1"}
                ),
                
                spacing="2",
                width="100%",
                padding="10px"
            ),
            
            # User info and logout
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.box(
                            rx.icon("user", size=18, color="white"),
                            bg="#3b82f6",
                            padding="8px",
                            border_radius="50%"
                        ),
                        rx.vstack(
                            rx.text(GRCState.current_user["name"], font_size="13px", color="white", font_weight="500"),
                            rx.text(GRCState.current_user["role"], font_size="11px", color="#94a3b8"),
                            spacing="0",
                            align_items="start"
                        ),
                        spacing="2",
                        width="100%"
                    ),
                    rx.button(
                        rx.icon("log-out", size=16),
                        " Logout",
                        on_click=AuthState.logout,
                        bg="#1e293b",
                        color="#cbd5e1",
                        width="100%",
                        margin_top="10px",
                        _hover={"bg": "#334155"}
                    ),
                    width="100%"
                ),
                padding="15px",
                margin_top="auto",
                border_top="1px solid #1e293b"
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


# Control Mapping Page - With expandable mapping details
@rx.page(route="/controls", title="Control Mapping - GRC Platform", on_load=ControlState.load_all_data)
def controls() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Control Mapping", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Unified controls mapped to framework requirements and policies", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            rx.box(
                rx.heading("Unified Controls (CCF)", font_size="24px", font_weight="600", margin_bottom="20px"),
                
                rx.foreach(
                    ControlState.unified_controls,
                    lambda ctrl: rx.box(
                        rx.vstack(
                            # Control header row
                            rx.hstack(
                                rx.vstack(
                                    rx.hstack(
                                        rx.badge(ctrl["ccf_id"], color_scheme="blue", font_family="monospace"),
                                        rx.text(ctrl["name"], font_size="18px", font_weight="600", color="#0f172a"),
                                        rx.badge(ctrl["status"], color_scheme=rx.cond(ctrl["status"] == "Effective", "green", rx.cond(ctrl["status"] == "Needs Improvement", "orange", "gray"))),
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
                                rx.button(
                                    rx.cond(
                                        ControlState.selected_control_id == ctrl["ccf_id"],
                                        rx.hstack(rx.icon("chevron-up", size=16), rx.text("Hide", font_size="13px"), spacing="1"),
                                        rx.hstack(rx.icon("chevron-down", size=16), rx.text("Mappings", font_size="13px"), spacing="1"),
                                    ),
                                    on_click=ControlState.toggle_control_details(ctrl["ccf_id"]),
                                    variant="outline",
                                    color="#3b82f6",
                                    border_color="#3b82f6",
                                    size="2",
                                    cursor="pointer"
                                ),
                                width="100%",
                                align_items="start"
                            ),
                            
                            # Expandable mapping details (uses computed vars)
                            rx.cond(
                                ControlState.selected_control_id == ctrl["ccf_id"],
                                rx.box(
                                    rx.grid(
                                        # Framework Mappings
                                        rx.box(
                                            rx.hstack(
                                                rx.icon("layers", size=18, color="#3b82f6"),
                                                rx.text("Framework Mappings", font_size="15px", font_weight="600", color="#1e40af"),
                                                spacing="2",
                                                margin_bottom="10px"
                                            ),
                                            rx.foreach(
                                                ControlState.selected_fw_mappings,
                                                lambda item: rx.box(
                                                    rx.text(item, font_size="13px", color="#0f172a"),
                                                    padding="10px",
                                                    bg="white",
                                                    border_radius="6px",
                                                    border="1px solid #dbeafe",
                                                    margin_bottom="6px"
                                                )
                                            ),
                                            padding="15px",
                                            bg="#eff6ff",
                                            border_radius="8px"
                                        ),
                                        # Policy Mappings
                                        rx.box(
                                            rx.hstack(
                                                rx.icon("file-text", size=18, color="#8b5cf6"),
                                                rx.text("Policy Mappings", font_size="15px", font_weight="600", color="#6d28d9"),
                                                spacing="2",
                                                margin_bottom="10px"
                                            ),
                                            rx.foreach(
                                                ControlState.selected_pol_mappings,
                                                lambda item: rx.box(
                                                    rx.text(item, font_size="13px", color="#0f172a"),
                                                    padding="10px",
                                                    bg="white",
                                                    border_radius="6px",
                                                    border="1px solid #e9d5ff",
                                                    margin_bottom="6px"
                                                )
                                            ),
                                            padding="15px",
                                            bg="#f5f3ff",
                                            border_radius="8px"
                                        ),
                                        columns="2",
                                        spacing="4",
                                        width="100%"
                                    ),
                                    margin_top="15px",
                                    padding_top="15px",
                                    border_top="1px dashed #cbd5e1"
                                ),
                                rx.fragment()
                            ),
                            
                            width="100%"
                        ),
                        bg="white",
                        padding="20px",
                        border_radius="12px",
                        border=rx.cond(
                            ControlState.selected_control_id == ctrl["ccf_id"],
                            "2px solid #3b82f6",
                            "1px solid #e2e8f0"
                        ),
                        margin_bottom="15px",
                        _hover={"border_color": "#3b82f6"}
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


# Policies Page - With expandable mapping details
@rx.page(route="/policies", title="Policies - GRC Platform", on_load=PolicyState.load_all_data)
def policies() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Policy Management", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Internal policies mapped to controls and frameworks", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            rx.box(
                rx.heading("Internal Policies", font_size="24px", font_weight="600", margin_bottom="20px"),
                
                rx.foreach(
                    PolicyState.policies,
                    lambda pol: rx.box(
                        rx.vstack(
                            # Policy header row
                            rx.hstack(
                                rx.vstack(
                                    rx.hstack(
                                        rx.badge(pol["policy_id"], color_scheme="purple", font_family="monospace"),
                                        rx.text(pol["name"], font_size="18px", font_weight="600"),
                                        rx.badge(pol["status"], color_scheme="green"),
                                        rx.badge(pol["category"], color_scheme="blue"),
                                        spacing="3"
                                    ),
                                    rx.text(pol["description"], font_size="14px", color="#64748b", margin_top="8px"),
                                    rx.hstack(
                                        rx.text("Owner: " + pol["owner"].to_string(), font_size="13px", color="#64748b"),
                                        rx.text("Last Review: " + pol["last_reviewed"].to_string(), font_size="13px", color="#64748b"),
                                        spacing="5",
                                        margin_top="8px"
                                    ),
                                    align_items="start",
                                    flex="1"
                                ),
                                rx.button(
                                    rx.cond(
                                        PolicyState.selected_policy_id == pol["policy_id"],
                                        rx.hstack(rx.icon("chevron-up", size=16), rx.text("Hide", font_size="13px"), spacing="1"),
                                        rx.hstack(rx.icon("chevron-down", size=16), rx.text("Details", font_size="13px"), spacing="1"),
                                    ),
                                    on_click=PolicyState.toggle_policy_details(pol["policy_id"]),
                                    variant="outline",
                                    color="#8b5cf6",
                                    border_color="#8b5cf6",
                                    size="2",
                                    cursor="pointer"
                                ),
                                width="100%",
                                align_items="start"
                            ),
                            
                            # Expandable details (uses computed vars)
                            rx.cond(
                                PolicyState.selected_policy_id == pol["policy_id"],
                                rx.box(
                                    rx.grid(
                                        # Mapped Controls
                                        rx.box(
                                            rx.hstack(
                                                rx.icon("shield-check", size=18, color="#3b82f6"),
                                                rx.text("Mapped Controls", font_size="15px", font_weight="600", color="#1e40af"),
                                                spacing="2",
                                                margin_bottom="10px"
                                            ),
                                            rx.foreach(
                                                PolicyState.selected_ctrl_mappings,
                                                lambda item: rx.box(
                                                    rx.text(item, font_size="13px", color="#0f172a"),
                                                    padding="10px",
                                                    bg="white",
                                                    border_radius="6px",
                                                    border="1px solid #dbeafe",
                                                    margin_bottom="6px"
                                                )
                                            ),
                                            padding="15px",
                                            bg="#eff6ff",
                                            border_radius="8px"
                                        ),
                                        # Applicable Frameworks
                                        rx.box(
                                            rx.hstack(
                                                rx.icon("layers", size=18, color="#10b981"),
                                                rx.text("Applicable Frameworks", font_size="15px", font_weight="600", color="#065f46"),
                                                spacing="2",
                                                margin_bottom="10px"
                                            ),
                                            rx.foreach(
                                                PolicyState.selected_fw_names,
                                                lambda fw: rx.box(
                                                    rx.hstack(
                                                        rx.icon("shield", size=14, color="#10b981"),
                                                        rx.text(fw, font_size="13px", color="#0f172a"),
                                                        spacing="2"
                                                    ),
                                                    padding="10px",
                                                    bg="white",
                                                    border_radius="6px",
                                                    border="1px solid #d1fae5",
                                                    margin_bottom="6px"
                                                )
                                            ),
                                            padding="15px",
                                            bg="#f0fdf4",
                                            border_radius="8px"
                                        ),
                                        columns="2",
                                        spacing="4",
                                        width="100%"
                                    ),
                                    margin_top="15px",
                                    padding_top="15px",
                                    border_top="1px dashed #cbd5e1"
                                ),
                                rx.fragment()
                            ),
                            
                            width="100%"
                        ),
                        bg="white",
                        padding="20px",
                        border_radius="12px",
                        border=rx.cond(
                            PolicyState.selected_policy_id == pol["policy_id"],
                            "2px solid #8b5cf6",
                            "1px solid #e2e8f0"
                        ),
                        margin_bottom="15px",
                        _hover={"border_color": "#8b5cf6"}
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

# Risks Page - With AI Suggestions
@rx.page(route="/risks", title="Risk Management - GRC Platform", on_load=RiskState.load_all_data)
def risks() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Risk Management", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Track and manage organizational risks", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            # AI Suggestions Section
            rx.box(
                rx.hstack(
                    rx.hstack(
                        rx.icon("sparkles", size=22, color="#f59e0b"),
                        rx.text("AI Risk Suggestions", font_size="20px", font_weight="600", color="#0f172a"),
                        spacing="2"
                    ),
                    rx.hstack(
                        rx.select(
                            ["General", "Financial Services", "Healthcare", "Technology", "Manufacturing", "Retail", "Energy"],
                            value=RiskState.ai_industry,
                            on_change=RiskState.set_ai_industry,
                            width="180px"
                        ),
                        rx.button(
                            rx.cond(
                                RiskState.ai_loading,
                                rx.hstack(rx.spinner(size="1"), rx.text("Generating...", font_size="13px"), spacing="2"),
                                rx.hstack(rx.icon("sparkles", size=16), rx.text("Suggest with AI", font_size="13px"), spacing="2"),
                            ),
                            on_click=RiskState.get_ai_suggestions,
                            bg="linear-gradient(135deg, #f59e0b 0%, #d97706 100%)",
                            color="white",
                            _hover={"opacity": 0.9},
                            border_radius="8px",
                            font_weight="600",
                            is_disabled=RiskState.ai_loading,
                            cursor="pointer"
                        ),
                        spacing="3"
                    ),
                    justify="between",
                    width="100%",
                    margin_bottom="15px"
                ),
                
                # AI Suggestions Results
                rx.cond(
                    RiskState.show_ai_suggestions,
                    rx.cond(
                        RiskState.ai_loading,
                        rx.center(
                            rx.vstack(
                                rx.spinner(size="3"),
                                rx.text("AI is analyzing risks...", font_size="14px", color="#64748b"),
                                spacing="3",
                                align_items="center"
                            ),
                            padding="40px"
                        ),
                        rx.cond(
                            RiskState.ai_suggestions.length() > 0,
                            rx.vstack(
                                rx.text("Click '+' to add a suggested risk to your register", font_size="13px", color="#64748b", margin_bottom="10px"),
                                rx.foreach(
                                    RiskState.ai_suggestions,
                                    lambda suggestion, idx: rx.box(
                                        rx.hstack(
                                            rx.vstack(
                                                rx.hstack(
                                                    rx.text(suggestion["name"], font_size="15px", font_weight="600", color="#0f172a"),
                                                    rx.badge(suggestion["category"], color_scheme="blue", size="1"),
                                                    spacing="2"
                                                ),
                                                rx.text(suggestion["description"], font_size="13px", color="#64748b"),
                                                rx.text("Inherent Score: " + suggestion["inherent_score"].to_string(), font_size="12px", color="#ef4444", font_weight="500"),
                                                align_items="start",
                                                flex="1",
                                                spacing="1"
                                            ),
                                            rx.button(
                                                rx.icon("plus", size=16),
                                                on_click=RiskState.add_suggested_risk(idx),
                                                bg="#10b981",
                                                color="white",
                                                size="2",
                                                _hover={"bg": "#059669"},
                                                cursor="pointer"
                                            ),
                                            width="100%",
                                            align_items="center"
                                        ),
                                        padding="12px",
                                        bg="#fffbeb",
                                        border="1px solid #fde68a",
                                        border_radius="8px",
                                        margin_bottom="8px"
                                    )
                                ),
                                width="100%"
                            ),
                            rx.text("No suggestions available", font_size="14px", color="#64748b", padding="20px")
                        )
                    ),
                    rx.fragment()
                ),
                
                bg="white",
                padding="24px",
                border_radius="12px",
                border="1px solid #fde68a",
                margin_bottom="20px",
                box_shadow="sm"
            ),
            
            # Risk Register
            rx.box(
                rx.hstack(
                    rx.heading("Risk Register", font_size="24px", font_weight="600"),
                    rx.button(rx.icon("plus", size=20), " Add Risk", on_click=RiskState.toggle_risk_form, bg="#3b82f6", color="white"),
                    justify="between", width="100%", margin_bottom="20px"
                ),
                
                rx.cond(
                    RiskState.show_risk_form,
                    rx.box(
                        rx.vstack(
                            rx.input(placeholder="Risk Name", value=RiskState.new_risk_name, on_change=RiskState.set_new_risk_name, width="100%"),
                            rx.text_area(placeholder="Description", value=RiskState.new_risk_description, on_change=RiskState.set_new_risk_description, width="100%"),
                            rx.select(["Security", "AI Governance", "Compliance", "Operations", "Financial", "Privacy"], value=RiskState.new_risk_category, on_change=RiskState.set_new_risk_category, width="100%"),
                            rx.input(placeholder="Owner", value=RiskState.new_risk_owner, on_change=RiskState.set_new_risk_owner, width="100%"),
                            rx.hstack(rx.button("Create", on_click=RiskState.create_risk, bg="#3b82f6", color="white"), rx.button("Cancel", on_click=RiskState.toggle_risk_form, bg="#e2e8f0"), spacing="3"),
                            spacing="4", width="100%"
                        ),
                        bg="#f8fafc", padding="20px", border_radius="8px", margin_bottom="20px"
                    ),
                    rx.fragment()
                ),
                
                rx.foreach(
                    RiskState.risks,
                    lambda risk: rx.box(
                        rx.hstack(
                            rx.vstack(
                                rx.hstack(rx.text(risk["name"], font_size="18px", font_weight="600"), rx.badge(risk["category"], color_scheme="blue"), spacing="3"),
                                rx.text(risk["description"], font_size="14px", color="#64748b", margin_top="5px"),
                                rx.text("Owner: " + risk["owner"].to_string(), font_size="13px", color="#64748b", margin_top="5px"),
                                align_items="start", flex="1"
                            ),
                            rx.hstack(
                                rx.vstack(rx.text("Inherent", font_size="11px", color="#64748b"), rx.text(risk["inherent_risk_score"], font_size="24px", font_weight="bold", color="#ef4444"), spacing="0", align_items="center"),
                                rx.vstack(rx.text("Residual", font_size="11px", color="#64748b"), rx.text(risk["residual_risk_score"], font_size="24px", font_weight="bold", color="#10b981"), spacing="0", align_items="center"),
                                spacing="4"
                            ),
                            width="100%", align_items="start"
                        ),
                        bg="white", padding="20px", border_radius="12px", border="1px solid #e2e8f0", margin_bottom="15px"
                    )
                ),
                
                bg="white", padding="30px", border_radius="12px", border="1px solid #e2e8f0"
            ),
            
            spacing="6", width="100%"
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
                            rx.icon("circle-x", size=24, color="#ef4444"),
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
                                    rx.text(kri["current_value"], font_size="32px", font_weight="bold", color="#3b82f6"),
                                    rx.text(kri["unit"], font_size="14px", color="#64748b", margin_left="5px"),
                                    align_items="baseline"
                                ),
                                rx.hstack(
                                    rx.box(bg="#10b981", width="12px", height="12px", border_radius="2px"),
                                    rx.text("Green", font_size="11px", color="#64748b"),
                                    rx.box(bg="#f59e0b", width="12px", height="12px", border_radius="2px"),
                                    rx.text("Yellow", font_size="11px", color="#64748b"),
                                    rx.box(bg="#ef4444", width="12px", height="12px", border_radius="2px"),
                                    rx.text("Red", font_size="11px", color="#64748b"),
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
                            rx.input(
                                placeholder="KRI ID (e.g., kri-001)",
                                value=KCIState.new_kci_kri_id,
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
                                    rx.text(kci["current_value"], font_size="32px", font_weight="bold", color="#8b5cf6"),
                                    rx.text(kci["unit"], font_size="14px", color="#64748b", margin_left="5px"),
                                    align_items="baseline"
                                ),
                                rx.hstack(
                                    rx.box(bg="#10b981", width="12px", height="12px", border_radius="2px"),
                                    rx.text("Green", font_size="11px", color="#64748b"),
                                    rx.box(bg="#f59e0b", width="12px", height="12px", border_radius="2px"),
                                    rx.text("Yellow", font_size="11px", color="#64748b"),
                                    rx.box(bg="#ef4444", width="12px", height="12px", border_radius="2px"),
                                    rx.text("Red", font_size="11px", color="#64748b"),
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
                    
                    # Network Visualization - Simplified 3-column layout
                    rx.grid(
                        # Column 1: Risks
                        rx.vstack(
                            rx.hstack(
                                rx.icon("alert-triangle", size=20, color="#ef4444"),
                                rx.text("RISKS", font_size="14px", font_weight="700", color="#ef4444"),
                                spacing="2"
                            ),
                            rx.foreach(
                                HeatmapState.risks,
                                lambda risk: rx.box(
                                    rx.vstack(
                                        rx.text(risk["name"], font_size="13px", font_weight="600", color="white"),
                                        rx.text("Score: " + risk["residual_risk_score"].to_string(), font_size="11px", color="rgba(255,255,255,0.8)"),
                                        spacing="1",
                                        align_items="start"
                                    ),
                                    bg="#ef4444",
                                    padding="12px 16px",
                                    border_radius="8px",
                                    width="100%",
                                    margin_bottom="8px"
                                )
                            ),
                            spacing="3",
                            align_items="stretch",
                            width="100%"
                        ),
                        
                        # Column 2: KRIs
                        rx.vstack(
                            rx.hstack(
                                rx.icon("bar-chart-3", size=20, color="#3b82f6"),
                                rx.text("KRIs", font_size="14px", font_weight="700", color="#3b82f6"),
                                spacing="2"
                            ),
                            rx.foreach(
                                HeatmapState.kris,
                                lambda kri: rx.box(
                                    rx.vstack(
                                        rx.text(kri["name"], font_size="13px", font_weight="600", color="#1e40af"),
                                        rx.hstack(
                                            rx.text("Value: " + kri["current_value"].to_string(), font_size="11px", color="#64748b"),
                                            rx.text(kri["unit"], font_size="10px", color="#94a3b8"),
                                            spacing="1"
                                        ),
                                        spacing="1",
                                        align_items="start"
                                    ),
                                    bg="#eff6ff",
                                    padding="12px 16px",
                                    border_radius="8px",
                                    border="1px solid #bfdbfe",
                                    width="100%",
                                    margin_bottom="8px"
                                )
                            ),
                            spacing="3",
                            align_items="stretch",
                            width="100%"
                        ),
                        
                        # Column 3: KCIs
                        rx.vstack(
                            rx.hstack(
                                rx.icon("target", size=20, color="#8b5cf6"),
                                rx.text("KCIs", font_size="14px", font_weight="700", color="#8b5cf6"),
                                spacing="2"
                            ),
                            rx.foreach(
                                HeatmapState.kcis,
                                lambda kci: rx.box(
                                    rx.vstack(
                                        rx.text(kci["name"], font_size="13px", font_weight="600", color="#6b21a8"),
                                        rx.hstack(
                                            rx.text("Value: " + kci["current_value"].to_string(), font_size="11px", color="#64748b"),
                                            rx.text(kci["unit"], font_size="10px", color="#94a3b8"),
                                            spacing="1"
                                        ),
                                        spacing="1",
                                        align_items="start"
                                    ),
                                    bg="#faf5ff",
                                    padding="12px 16px",
                                    border_radius="8px",
                                    border="1px solid #e9d5ff",
                                    width="100%",
                                    margin_bottom="8px"
                                )
                            ),
                            spacing="3",
                            align_items="stretch",
                            width="100%"
                        ),
                        
                        columns="3",
                        spacing="6",
                        width="100%"
                    ),
                    
                    # Flow arrows
                    rx.hstack(
                        rx.box(
                            rx.hstack(
                                rx.icon("alert-triangle", size=16, color="#ef4444"),
                                rx.text("Risks", font_size="12px", color="#64748b"),
                                spacing="1"
                            ),
                            padding="8px 12px",
                            bg="#fef2f2",
                            border_radius="6px"
                        ),
                        rx.icon("arrow-right", size=20, color="#64748b"),
                        rx.box(
                            rx.hstack(
                                rx.icon("bar-chart-3", size=16, color="#3b82f6"),
                                rx.text("KRIs", font_size="12px", color="#64748b"),
                                spacing="1"
                            ),
                            padding="8px 12px",
                            bg="#eff6ff",
                            border_radius="6px"
                        ),
                        rx.icon("arrow-right", size=20, color="#64748b"),
                        rx.box(
                            rx.hstack(
                                rx.icon("target", size=16, color="#8b5cf6"),
                                rx.text("KCIs", font_size="12px", color="#64748b"),
                                spacing="1"
                            ),
                            padding="8px 12px",
                            bg="#faf5ff",
                            border_radius="6px"
                        ),
                        rx.icon("arrow-right", size=20, color="#64748b"),
                        rx.box(
                            rx.hstack(
                                rx.icon("shield", size=16, color="#10b981"),
                                rx.text("Controls", font_size="12px", color="#64748b"),
                                spacing="1"
                            ),
                            padding="8px 12px",
                            bg="#f0fdf4",
                            border_radius="6px"
                        ),
                        spacing="3",
                        justify="center",
                        margin_top="30px",
                        padding="15px",
                        bg="#f8fafc",
                        border_radius="10px"
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


# AI Models Page
@rx.page(route="/ai-models", title="AI Models - GRC Platform", on_load=AIGovernanceState.load_all_data)
def ai_models() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("AI Model Registry", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Track and govern all AI/ML models in your organization", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            # Stats
            rx.grid(
                rx.box(
                    rx.hstack(
                        rx.box(rx.icon("brain", size=24, color="#8b5cf6"), bg="#faf5ff", padding="10px", border_radius="50%"),
                        rx.vstack(
                            rx.text("Total Models", font_size="14px", color="#64748b"),
                            rx.text(AIGovernanceState.total_ai_models, font_size="28px", font_weight="bold", color="#0f172a"),
                            spacing="0", align_items="start"
                        ),
                        spacing="4"
                    ),
                    bg="white", padding="20px", border_radius="12px", border="1px solid #e2e8f0"
                ),
                rx.box(
                    rx.hstack(
                        rx.box(rx.icon("rocket", size=24, color="#10b981"), bg="#f0fdf4", padding="10px", border_radius="50%"),
                        rx.vstack(
                            rx.text("In Production", font_size="14px", color="#64748b"),
                            rx.text(AIGovernanceState.production_ai_models, font_size="28px", font_weight="bold", color="#10b981"),
                            spacing="0", align_items="start"
                        ),
                        spacing="4"
                    ),
                    bg="white", padding="20px", border_radius="12px", border="1px solid #e2e8f0"
                ),
                rx.box(
                    rx.hstack(
                        rx.box(rx.icon("alert-triangle", size=24, color="#ef4444"), bg="#fef2f2", padding="10px", border_radius="50%"),
                        rx.vstack(
                            rx.text("High Risk", font_size="14px", color="#64748b"),
                            rx.text(AIGovernanceState.high_risk_ai_models, font_size="28px", font_weight="bold", color="#ef4444"),
                            spacing="0", align_items="start"
                        ),
                        spacing="4"
                    ),
                    bg="white", padding="20px", border_radius="12px", border="1px solid #e2e8f0"
                ),
                columns="3", spacing="4", width="100%", margin_bottom="30px"
            ),
            
            # Models Section
            rx.box(
                rx.hstack(
                    rx.heading("Registered Models", font_size="24px", font_weight="600"),
                    rx.button(
                        rx.icon("plus", size=20), " Register Model",
                        on_click=AIGovernanceState.toggle_model_form,
                        bg="#8b5cf6", color="white", _hover={"bg": "#7c3aed"},
                        padding="12px 20px", border_radius="8px", font_weight="600"
                    ),
                    justify="between", width="100%", margin_bottom="20px"
                ),
                
                # Create Form
                rx.cond(
                    AIGovernanceState.show_model_form,
                    rx.box(
                        rx.vstack(
                            rx.grid(
                                rx.input(placeholder="Model Name *", value=AIGovernanceState.new_model_name, on_change=AIGovernanceState.set_new_model_name),
                                rx.select(["Classification", "Regression", "NLP Classification", "Anomaly Detection", "Time Series", "Recommendation", "Computer Vision", "Generative"], value=AIGovernanceState.new_model_type, on_change=AIGovernanceState.set_new_model_type),
                                rx.input(placeholder="Version", value=AIGovernanceState.new_model_version, on_change=AIGovernanceState.set_new_model_version),
                                rx.select(["Development", "Testing", "Staging", "Production", "Deprecated"], value=AIGovernanceState.new_model_status, on_change=AIGovernanceState.set_new_model_status),
                                rx.select(["Low", "Medium", "High", "Critical"], value=AIGovernanceState.new_model_risk_level, on_change=AIGovernanceState.set_new_model_risk_level),
                                rx.input(placeholder="Owner *", value=AIGovernanceState.new_model_owner, on_change=AIGovernanceState.set_new_model_owner),
                                columns="3", spacing="3", width="100%"
                            ),
                            rx.input(placeholder="Department", value=AIGovernanceState.new_model_department, on_change=AIGovernanceState.set_new_model_department, width="100%"),
                            rx.text_area(placeholder="Purpose / Description", value=AIGovernanceState.new_model_purpose, on_change=AIGovernanceState.set_new_model_purpose, width="100%"),
                            rx.hstack(
                                rx.button("Register Model", on_click=AIGovernanceState.create_ai_model, bg="#8b5cf6", color="white"),
                                rx.button("Cancel", on_click=AIGovernanceState.toggle_model_form, bg="#e2e8f0"),
                                spacing="3"
                            ),
                            spacing="4", width="100%"
                        ),
                        bg="#faf5ff", padding="20px", border_radius="8px", margin_bottom="20px"
                    ),
                    rx.fragment()
                ),
                
                # Models List
                rx.foreach(
                    AIGovernanceState.ai_models,
                    lambda model: rx.box(
                        rx.hstack(
                            rx.vstack(
                                rx.hstack(
                                    rx.text(model["name"], font_size="18px", font_weight="600"),
                                    rx.badge(model["version"], color_scheme="gray"),
                                    rx.badge(model["status"], color_scheme=rx.cond(model["status"] == "Production", "green", rx.cond(model["status"] == "Testing", "yellow", "gray"))),
                                    rx.badge(model["risk_level"], color_scheme=rx.cond(model["risk_level"] == "Critical", "red", rx.cond(model["risk_level"] == "High", "orange", rx.cond(model["risk_level"] == "Medium", "yellow", "green")))),
                                    spacing="2"
                                ),
                                rx.text(model["purpose"], font_size="14px", color="#64748b", margin_top="5px"),
                                rx.hstack(
                                    rx.text("Type: " + model["type"].to_string(), font_size="13px", color="#64748b"),
                                    rx.text("Owner: " + model["owner"].to_string(), font_size="13px", color="#64748b"),
                                    rx.text("Dept: " + model["department"].to_string(), font_size="13px", color="#64748b"),
                                    spacing="5", margin_top="10px"
                                ),
                                align_items="start", flex="1"
                            ),
                            rx.vstack(
                                rx.cond(
                                    model["accuracy"] != None,
                                    rx.text("Accuracy: " + model["accuracy"].to_string(), font_size="13px", color="#64748b"),
                                    rx.fragment()
                                ),
                                rx.cond(
                                    model["pii_involved"],
                                    rx.badge("PII Data", color_scheme="red"),
                                    rx.fragment()
                                ),
                                rx.cond(
                                    model["automated_decisions"],
                                    rx.badge("Auto Decisions", color_scheme="orange"),
                                    rx.fragment()
                                ),
                                align_items="end", spacing="2"
                            ),
                            width="100%", align_items="start"
                        ),
                        bg="white", padding="20px", border_radius="12px", border="1px solid #e2e8f0", margin_bottom="15px"
                    )
                ),
                
                bg="white", padding="30px", border_radius="12px", border="1px solid #e2e8f0"
            ),
            
            spacing="6", width="100%"
        )
    )


# AI Assessments Page
@rx.page(route="/ai-assessments", title="AI Assessments - GRC Platform", on_load=AIGovernanceState.load_all_data)
def ai_assessments() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("AI Risk Assessments", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Evaluate AI models for bias, privacy, security, and transparency risks", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            rx.box(
                rx.hstack(
                    rx.heading("Assessment Records", font_size="24px", font_weight="600"),
                    rx.button(
                        rx.icon("plus", size=20), " New Assessment",
                        on_click=AIGovernanceState.toggle_assessment_form,
                        bg="#3b82f6", color="white", _hover={"bg": "#2563eb"},
                        padding="12px 20px", border_radius="8px", font_weight="600"
                    ),
                    justify="between", width="100%", margin_bottom="20px"
                ),
                
                # Create Form
                rx.cond(
                    AIGovernanceState.show_assessment_form,
                    rx.box(
                        rx.vstack(
                            rx.input(placeholder="Model ID to assess", value=AIGovernanceState.assessment_model_id, on_change=AIGovernanceState.set_assessment_model_id, width="100%"),
                            rx.grid(
                                rx.vstack(rx.text("Bias Risk", font_size="13px", color="#64748b"), rx.select(["Low", "Medium", "High", "Critical"], value=AIGovernanceState.assessment_bias_risk, on_change=AIGovernanceState.set_assessment_bias_risk), spacing="1"),
                                rx.vstack(rx.text("Privacy Risk", font_size="13px", color="#64748b"), rx.select(["Low", "Medium", "High", "Critical"], value=AIGovernanceState.assessment_privacy_risk, on_change=AIGovernanceState.set_assessment_privacy_risk), spacing="1"),
                                rx.vstack(rx.text("Security Risk", font_size="13px", color="#64748b"), rx.select(["Low", "Medium", "High", "Critical"], value=AIGovernanceState.assessment_security_risk, on_change=AIGovernanceState.set_assessment_security_risk), spacing="1"),
                                rx.vstack(rx.text("Transparency Risk", font_size="13px", color="#64748b"), rx.select(["Low", "Medium", "High", "Critical"], value=AIGovernanceState.assessment_transparency_risk, on_change=AIGovernanceState.set_assessment_transparency_risk), spacing="1"),
                                columns="4", spacing="3", width="100%"
                            ),
                            rx.text_area(placeholder="Findings (one per line)", value=AIGovernanceState.assessment_findings, on_change=AIGovernanceState.set_assessment_findings, width="100%"),
                            rx.text_area(placeholder="Recommendations (one per line)", value=AIGovernanceState.assessment_recommendations, on_change=AIGovernanceState.set_assessment_recommendations, width="100%"),
                            rx.hstack(
                                rx.button("Create Assessment", on_click=AIGovernanceState.create_assessment, bg="#3b82f6", color="white"),
                                rx.button("Cancel", on_click=AIGovernanceState.toggle_assessment_form, bg="#e2e8f0"),
                                spacing="3"
                            ),
                            spacing="4", width="100%"
                        ),
                        bg="#eff6ff", padding="20px", border_radius="8px", margin_bottom="20px"
                    ),
                    rx.fragment()
                ),
                
                # Assessments List
                rx.foreach(
                    AIGovernanceState.ai_assessments,
                    lambda assess: rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.text(assess["model_name"], font_size="18px", font_weight="600"),
                                rx.badge(assess["overall_risk"], color_scheme=rx.cond(assess["overall_risk"] == "Critical", "red", rx.cond(assess["overall_risk"] == "High", "orange", rx.cond(assess["overall_risk"] == "Medium", "yellow", "green")))),
                                rx.badge(assess["status"], color_scheme="blue"),
                                spacing="2"
                            ),
                            rx.text("Assessed: " + assess["assessment_date"].to_string() + " by " + assess["assessor"].to_string(), font_size="13px", color="#64748b"),
                            rx.grid(
                                rx.box(rx.text("Bias", font_size="12px", color="#64748b"), rx.badge(assess["bias_risk"], color_scheme=rx.cond(assess["bias_risk"] == "High", "orange", rx.cond(assess["bias_risk"] == "Critical", "red", "gray"))), padding="10px", bg="#f8fafc", border_radius="6px"),
                                rx.box(rx.text("Privacy", font_size="12px", color="#64748b"), rx.badge(assess["privacy_risk"], color_scheme=rx.cond(assess["privacy_risk"] == "High", "orange", rx.cond(assess["privacy_risk"] == "Critical", "red", "gray"))), padding="10px", bg="#f8fafc", border_radius="6px"),
                                rx.box(rx.text("Security", font_size="12px", color="#64748b"), rx.badge(assess["security_risk"], color_scheme=rx.cond(assess["security_risk"] == "High", "orange", rx.cond(assess["security_risk"] == "Critical", "red", "gray"))), padding="10px", bg="#f8fafc", border_radius="6px"),
                                rx.box(rx.text("Transparency", font_size="12px", color="#64748b"), rx.badge(assess["transparency_risk"], color_scheme=rx.cond(assess["transparency_risk"] == "High", "orange", rx.cond(assess["transparency_risk"] == "Critical", "red", "gray"))), padding="10px", bg="#f8fafc", border_radius="6px"),
                                columns="4", spacing="3", width="100%", margin_top="15px"
                            ),
                            align_items="start", width="100%"
                        ),
                        bg="white", padding="20px", border_radius="12px", border="1px solid #e2e8f0", margin_bottom="15px"
                    )
                ),
                
                bg="white", padding="30px", border_radius="12px", border="1px solid #e2e8f0"
            ),
            
            spacing="6", width="100%"
        )
    )


# Connectors Page
@rx.page(route="/connectors", title="Connectors - GRC Platform", on_load=ConnectorState.load_all_data)
def connectors() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Integration Connectors", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Connect to cloud services for automated control testing", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            rx.box(
                rx.heading("Available Connectors", font_size="24px", font_weight="600", margin_bottom="20px"),
                
                rx.foreach(
                    ConnectorState.connectors,
                    lambda conn: rx.box(
                        rx.hstack(
                            rx.box(
                                rx.icon(
                                    rx.cond(conn["provider"] == "AWS", "cloud", rx.cond(conn["provider"] == "GitHub", "github", rx.cond(conn["provider"] == "Okta", "key", "server"))),
                                    size=28,
                                    color=rx.cond(conn["status"] == "Connected", "#10b981", "#64748b")
                                ),
                                bg=rx.cond(conn["status"] == "Connected", "#f0fdf4", "#f8fafc"),
                                padding="15px",
                                border_radius="12px"
                            ),
                            rx.vstack(
                                rx.hstack(
                                    rx.text(conn["name"], font_size="18px", font_weight="600"),
                                    rx.badge(conn["status"], color_scheme=rx.cond(conn["status"] == "Connected", "green", "gray")),
                                    spacing="2"
                                ),
                                rx.text("Provider: " + conn["provider"].to_string() + " | Type: " + conn["type"].to_string(), font_size="14px", color="#64748b"),
                                rx.cond(
                                    conn["last_sync"] != None,
                                    rx.text("Last sync: " + conn["last_sync"].to_string(), font_size="13px", color="#94a3b8"),
                                    rx.fragment()
                                ),
                                align_items="start", flex="1"
                            ),
                            rx.button(
                                rx.cond(conn["status"] == "Connected", "Disconnect", "Connect"),
                                on_click=lambda: ConnectorState.toggle_connector(conn["id"], conn["status"]),
                                bg=rx.cond(conn["status"] == "Connected", "#ef4444", "#10b981"),
                                color="white",
                                _hover={"opacity": 0.8}
                            ),
                            width="100%", align_items="center", spacing="4"
                        ),
                        bg="white", padding="20px", border_radius="12px", border="1px solid #e2e8f0", margin_bottom="15px"
                    )
                ),
                
                bg="white", padding="30px", border_radius="12px", border="1px solid #e2e8f0"
            ),
            
            spacing="6", width="100%"
        )
    )


# Audit Logs Page
@rx.page(route="/audit-logs", title="Audit Logs - GRC Platform", on_load=AuditLogState.load_all_data)
def audit_logs() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Audit Logs", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Track all user actions and system events", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            rx.box(
                rx.heading("Recent Activity", font_size="24px", font_weight="600", margin_bottom="20px"),
                
                rx.foreach(
                    AuditLogState.audit_logs,
                    lambda log: rx.box(
                        rx.hstack(
                            rx.box(
                                rx.icon(
                                    rx.cond(log["action"] == "LOGIN", "log-in", rx.cond(log["action"] == "LOGOUT", "log-out", rx.cond(log["action"] == "CREATE", "plus", rx.cond(log["action"] == "UPDATE", "pencil", rx.cond(log["action"] == "DELETE", "trash", "eye"))))),
                                    size=18,
                                    color=rx.cond(log["action"] == "DELETE", "#ef4444", rx.cond(log["action"] == "CREATE", "#10b981", "#3b82f6"))
                                ),
                                bg="#f8fafc",
                                padding="10px",
                                border_radius="8px"
                            ),
                            rx.vstack(
                                rx.hstack(
                                    rx.badge(log["action"], color_scheme=rx.cond(log["action"] == "DELETE", "red", rx.cond(log["action"] == "CREATE", "green", "blue"))),
                                    rx.text(log["resource"], font_size="14px", font_weight="500"),
                                    spacing="2"
                                ),
                                rx.text(log["details"], font_size="14px", color="#64748b"),
                                rx.text(log["user_email"].to_string() + " | " + log["timestamp"].to_string(), font_size="12px", color="#94a3b8"),
                                align_items="start", spacing="1"
                            ),
                            width="100%", spacing="3"
                        ),
                        bg="white", padding="15px", border_radius="8px", border="1px solid #e2e8f0", margin_bottom="10px"
                    )
                ),
                
                bg="white", padding="30px", border_radius="12px", border="1px solid #e2e8f0"
            ),
            
            spacing="6", width="100%"
        )
    )


# Compliance Gap Analysis Page - AI Powered
@rx.page(route="/gap-analysis", title="Gap Analysis - GRC Platform", on_load=GapAnalysisState.load_all_data)
def gap_analysis() -> rx.Component:
    return layout(
        rx.vstack(
            # Header
            rx.hstack(
                rx.vstack(
                    rx.heading("Compliance Gap Analysis", font_size="40px", font_weight="bold", color="#0f172a"),
                    rx.text("AI-powered assessment of your compliance posture against any framework", font_size="18px", color="#64748b"),
                    spacing="2",
                    align_items="start"
                ),
                rx.badge("Powered by Gemini AI", color_scheme="amber", size="2", variant="solid"),
                justify="between",
                width="100%",
                align_items="center",
                margin_bottom="30px"
            ),
            
            # Framework Selection & Run
            rx.box(
                rx.hstack(
                    rx.vstack(
                        rx.text("Select Framework", font_size="14px", font_weight="600", color="#374151"),
                        rx.select(
                            GapAnalysisState.framework_names,
                            value=GapAnalysisState.selected_framework,
                            on_change=GapAnalysisState.set_selected_framework,
                            placeholder="Choose a compliance framework...",
                            width="350px",
                        ),
                        spacing="1",
                        align_items="start"
                    ),
                    rx.button(
                        rx.cond(
                            GapAnalysisState.analysis_loading,
                            rx.hstack(rx.spinner(size="1"), rx.text("Analyzing...", font_size="14px"), spacing="2"),
                            rx.hstack(rx.icon("sparkles", size=18), rx.text("Run Gap Analysis", font_size="14px"), spacing="2"),
                        ),
                        on_click=GapAnalysisState.run_gap_analysis,
                        bg="linear-gradient(135deg, #f59e0b 0%, #d97706 100%)",
                        color="white",
                        size="3",
                        _hover={"opacity": 0.9},
                        border_radius="10px",
                        font_weight="700",
                        is_disabled=GapAnalysisState.analysis_loading,
                        cursor="pointer",
                        padding_x="28px"
                    ),
                    spacing="5",
                    align_items="end"
                ),
                bg="white",
                padding="24px",
                border_radius="12px",
                border="1px solid #e2e8f0",
                margin_bottom="20px"
            ),
            
            # Loading state
            rx.cond(
                GapAnalysisState.analysis_loading,
                rx.center(
                    rx.vstack(
                        rx.spinner(size="3"),
                        rx.text("AI is analyzing your compliance posture...", font_size="16px", color="#64748b"),
                        rx.text("This may take 15-30 seconds", font_size="13px", color="#94a3b8"),
                        spacing="3",
                        align_items="center"
                    ),
                    padding="60px",
                    bg="white",
                    border_radius="12px",
                    border="1px solid #e2e8f0"
                ),
                rx.fragment()
            ),
            
            # Results
            rx.cond(
                GapAnalysisState.analysis_complete,
                rx.vstack(
                    # Score Cards Row
                    rx.grid(
                        # Overall Score
                        rx.box(
                            rx.vstack(
                                rx.text("Compliance Score", font_size="13px", color="#64748b", font_weight="500"),
                                rx.text(
                                    GapAnalysisState.overall_score,
                                    font_size="52px",
                                    font_weight="bold",
                                    color=rx.cond(
                                        GapAnalysisState.overall_score >= 80,
                                        "#10b981",
                                        rx.cond(GapAnalysisState.overall_score >= 60, "#f59e0b", "#ef4444")
                                    )
                                ),
                                rx.text("/ 100", font_size="16px", color="#94a3b8", margin_top="-10px"),
                                align_items="center",
                                spacing="1"
                            ),
                            bg="white",
                            padding="24px",
                            border_radius="12px",
                            border="1px solid #e2e8f0",
                            text_align="center"
                        ),
                        # Maturity Level
                        rx.box(
                            rx.vstack(
                                rx.text("Maturity Level", font_size="13px", color="#64748b", font_weight="500"),
                                rx.text(GapAnalysisState.maturity_level, font_size="28px", font_weight="bold", color="#1e40af"),
                                rx.text(GapAnalysisState.selected_framework, font_size="14px", color="#94a3b8"),
                                align_items="center",
                                spacing="1"
                            ),
                            bg="white",
                            padding="24px",
                            border_radius="12px",
                            border="1px solid #e2e8f0",
                            text_align="center"
                        ),
                        # Gaps Found
                        rx.box(
                            rx.vstack(
                                rx.text("Gaps Found", font_size="13px", color="#64748b", font_weight="500"),
                                rx.text(GapAnalysisState.critical_gaps.length(), font_size="52px", font_weight="bold", color="#ef4444"),
                                rx.text("requiring attention", font_size="14px", color="#94a3b8"),
                                align_items="center",
                                spacing="1"
                            ),
                            bg="white",
                            padding="24px",
                            border_radius="12px",
                            border="1px solid #e2e8f0",
                            text_align="center"
                        ),
                        # Quick Wins
                        rx.box(
                            rx.vstack(
                                rx.text("Quick Wins", font_size="13px", color="#64748b", font_weight="500"),
                                rx.text(GapAnalysisState.quick_wins.length(), font_size="52px", font_weight="bold", color="#10b981"),
                                rx.text("easy improvements", font_size="14px", color="#94a3b8"),
                                align_items="center",
                                spacing="1"
                            ),
                            bg="white",
                            padding="24px",
                            border_radius="12px",
                            border="1px solid #e2e8f0",
                            text_align="center"
                        ),
                        columns="4",
                        spacing="4",
                        width="100%",
                        margin_bottom="20px"
                    ),
                    
                    # Executive Summary
                    rx.box(
                        rx.hstack(
                            rx.icon("file-text", size=20, color="#3b82f6"),
                            rx.text("Executive Summary", font_size="18px", font_weight="600", color="#0f172a"),
                            spacing="2"
                        ),
                        rx.text(GapAnalysisState.summary, font_size="15px", color="#374151", margin_top="12px", line_height="1.7"),
                        bg="white",
                        padding="24px",
                        border_radius="12px",
                        border="1px solid #e2e8f0",
                        margin_bottom="20px"
                    ),
                    
                    # Two column layout: Strengths + Critical Gaps
                    rx.grid(
                        # Strengths
                        rx.box(
                            rx.hstack(
                                rx.icon("check-circle", size=20, color="#10b981"),
                                rx.text("Strengths", font_size="18px", font_weight="600", color="#065f46"),
                                spacing="2",
                                margin_bottom="15px"
                            ),
                            rx.foreach(
                                GapAnalysisState.strengths,
                                lambda s: rx.box(
                                    rx.hstack(
                                        rx.icon("shield-check", size=16, color="#10b981"),
                                        rx.text(s, font_size="14px", color="#374151"),
                                        spacing="2",
                                        align_items="start"
                                    ),
                                    padding="12px",
                                    bg="#f0fdf4",
                                    border_radius="8px",
                                    border="1px solid #bbf7d0",
                                    margin_bottom="8px"
                                )
                            ),
                            bg="white",
                            padding="24px",
                            border_radius="12px",
                            border="1px solid #e2e8f0"
                        ),
                        # Critical Gaps
                        rx.box(
                            rx.hstack(
                                rx.icon("alert-triangle", size=20, color="#ef4444"),
                                rx.text("Critical Gaps", font_size="18px", font_weight="600", color="#991b1b"),
                                spacing="2",
                                margin_bottom="15px"
                            ),
                            rx.foreach(
                                GapAnalysisState.critical_gaps,
                                lambda g, idx: rx.box(
                                    rx.vstack(
                                        rx.hstack(
                                            rx.icon("alert-circle", size=16, color="#ef4444"),
                                            rx.text(g, font_size="14px", font_weight="500", color="#374151"),
                                            spacing="2",
                                            align_items="start"
                                        ),
                                        rx.cond(
                                            idx < GapAnalysisState.gap_recommendations.length(),
                                            rx.hstack(
                                                rx.icon("lightbulb", size=14, color="#f59e0b"),
                                                rx.text(GapAnalysisState.gap_recommendations[idx], font_size="13px", color="#92400e", font_style="italic"),
                                                spacing="2",
                                                margin_top="4px",
                                                align_items="start"
                                            ),
                                            rx.fragment()
                                        ),
                                        spacing="1"
                                    ),
                                    padding="12px",
                                    bg="#fef2f2",
                                    border_radius="8px",
                                    border="1px solid #fecaca",
                                    margin_bottom="8px"
                                )
                            ),
                            bg="white",
                            padding="24px",
                            border_radius="12px",
                            border="1px solid #e2e8f0"
                        ),
                        columns="2",
                        spacing="4",
                        width="100%",
                        margin_bottom="20px"
                    ),
                    
                    # Improvements Table
                    rx.box(
                        rx.hstack(
                            rx.icon("arrow-up-circle", size=20, color="#3b82f6"),
                            rx.text("Improvement Areas", font_size="18px", font_weight="600", color="#0f172a"),
                            spacing="2",
                            margin_bottom="15px"
                        ),
                        rx.foreach(
                            GapAnalysisState.improvements,
                            lambda imp: rx.box(
                                rx.hstack(
                                    rx.icon("arrow-right", size=16, color="#3b82f6"),
                                    rx.text(imp, font_size="14px", color="#374151"),
                                    spacing="2",
                                    align_items="start"
                                ),
                                padding="12px",
                                bg="#eff6ff",
                                border_radius="8px",
                                border="1px solid #bfdbfe",
                                margin_bottom="8px"
                            )
                        ),
                        bg="white",
                        padding="24px",
                        border_radius="12px",
                        border="1px solid #e2e8f0",
                        margin_bottom="20px"
                    ),
                    
                    # Quick Wins + Roadmap
                    rx.grid(
                        # Quick Wins
                        rx.box(
                            rx.hstack(
                                rx.icon("zap", size=20, color="#10b981"),
                                rx.text("Quick Wins", font_size="18px", font_weight="600", color="#065f46"),
                                spacing="2",
                                margin_bottom="15px"
                            ),
                            rx.foreach(
                                GapAnalysisState.quick_wins,
                                lambda qw, idx: rx.box(
                                    rx.hstack(
                                        rx.box(
                                            rx.text((idx + 1).to(str), font_size="12px", font_weight="bold", color="white"),
                                            bg="#10b981",
                                            width="24px",
                                            height="24px",
                                            border_radius="50%",
                                            display="flex",
                                            align_items="center",
                                            justify_content="center",
                                            flex_shrink="0"
                                        ),
                                        rx.text(qw, font_size="14px", color="#374151"),
                                        spacing="3",
                                        align_items="center"
                                    ),
                                    padding="12px",
                                    bg="white",
                                    border_radius="8px",
                                    border="1px solid #d1fae5",
                                    margin_bottom="8px"
                                )
                            ),
                            bg="#f0fdf4",
                            padding="24px",
                            border_radius="12px",
                            border="1px solid #bbf7d0"
                        ),
                        # Roadmap
                        rx.box(
                            rx.hstack(
                                rx.icon("map", size=20, color="#8b5cf6"),
                                rx.text("Remediation Roadmap", font_size="18px", font_weight="600", color="#5b21b6"),
                                spacing="2",
                                margin_bottom="15px"
                            ),
                            rx.foreach(
                                GapAnalysisState.roadmap_phases,
                                lambda phase, idx: rx.box(
                                    rx.vstack(
                                        rx.text(phase, font_size="15px", font_weight="600", color="#5b21b6"),
                                        rx.cond(
                                            idx < GapAnalysisState.roadmap_actions.length(),
                                            rx.text(GapAnalysisState.roadmap_actions[idx], font_size="13px", color="#374151"),
                                            rx.fragment()
                                        ),
                                        spacing="1",
                                        align_items="start"
                                    ),
                                    padding="14px",
                                    bg="white",
                                    border_radius="8px",
                                    border="1px solid #ddd6fe",
                                    border_left="4px solid #8b5cf6",
                                    margin_bottom="10px"
                                )
                            ),
                            bg="#f5f3ff",
                            padding="24px",
                            border_radius="12px",
                            border="1px solid #ddd6fe"
                        ),
                        columns="2",
                        spacing="4",
                        width="100%"
                    ),
                    
                    width="100%"
                ),
                rx.fragment()
            ),
            
            spacing="4",
            width="100%"
        )
    )


# Audit Planning Page
@rx.page(route="/audit-planning", title="Audit Planning - GRC Platform", on_load=AuditManagementState.load_audit_data)
def audit_planning() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Internal Audit Management", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Plan audits, track findings, and manage remediation", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            # Stats Row
            rx.grid(
                rx.box(
                    rx.vstack(
                        rx.text("Total Audits", font_size="13px", color="#64748b"),
                        rx.text(AuditManagementState.audit_stats["total"], font_size="36px", font_weight="bold", color="#0f172a"),
                        align_items="center", spacing="1"
                    ),
                    bg="white", padding="20px", border_radius="12px", border="1px solid #e2e8f0", text_align="center"
                ),
                rx.box(
                    rx.vstack(
                        rx.text("Planned", font_size="13px", color="#64748b"),
                        rx.text(AuditManagementState.audit_stats["planned"], font_size="36px", font_weight="bold", color="#3b82f6"),
                        align_items="center", spacing="1"
                    ),
                    bg="white", padding="20px", border_radius="12px", border="1px solid #e2e8f0", text_align="center"
                ),
                rx.box(
                    rx.vstack(
                        rx.text("In Progress", font_size="13px", color="#64748b"),
                        rx.text(AuditManagementState.audit_stats["in_progress"], font_size="36px", font_weight="bold", color="#f59e0b"),
                        align_items="center", spacing="1"
                    ),
                    bg="white", padding="20px", border_radius="12px", border="1px solid #e2e8f0", text_align="center"
                ),
                rx.box(
                    rx.vstack(
                        rx.text("Completed", font_size="13px", color="#64748b"),
                        rx.text(AuditManagementState.audit_stats["completed"], font_size="36px", font_weight="bold", color="#10b981"),
                        align_items="center", spacing="1"
                    ),
                    bg="white", padding="20px", border_radius="12px", border="1px solid #e2e8f0", text_align="center"
                ),
                rx.box(
                    rx.vstack(
                        rx.text("Open Findings", font_size="13px", color="#64748b"),
                        rx.text(AuditManagementState.audit_stats["open_findings"], font_size="36px", font_weight="bold", color="#ef4444"),
                        align_items="center", spacing="1"
                    ),
                    bg="white", padding="20px", border_radius="12px", border="1px solid #e2e8f0", text_align="center"
                ),
                columns="5", spacing="4", width="100%", margin_bottom="20px"
            ),
            
            # Create Audit Button + Form
            rx.box(
                rx.hstack(
                    rx.heading("Audit Plans", font_size="24px", font_weight="600"),
                    rx.button(
                        rx.icon("plus", size=18), " New Audit Plan",
                        on_click=AuditManagementState.toggle_audit_form,
                        bg="#3b82f6", color="white", cursor="pointer"
                    ),
                    justify="between", width="100%", margin_bottom="20px"
                ),
                
                # New Audit Form
                rx.cond(
                    AuditManagementState.show_audit_form,
                    rx.box(
                        rx.vstack(
                            rx.text("Create New Audit Plan", font_size="18px", font_weight="600", color="#0f172a"),
                            rx.grid(
                                rx.vstack(
                                    rx.text("Audit Name *", font_size="13px", color="#64748b"),
                                    rx.input(placeholder="e.g., ISO 27001 Annual Audit 2026", value=AuditManagementState.new_audit_name, on_change=AuditManagementState.set_new_audit_name, width="100%"),
                                    spacing="1"
                                ),
                                rx.vstack(
                                    rx.text("Framework *", font_size="13px", color="#64748b"),
                                    rx.select(AuditManagementState.framework_options, value=AuditManagementState.new_audit_framework, on_change=AuditManagementState.set_new_audit_framework, placeholder="Select framework...", width="100%"),
                                    spacing="1"
                                ),
                                columns="2", spacing="4", width="100%"
                            ),
                            rx.grid(
                                rx.vstack(
                                    rx.text("Lead Auditor", font_size="13px", color="#64748b"),
                                    rx.input(placeholder="Auditor name", value=AuditManagementState.new_audit_auditor, on_change=AuditManagementState.set_new_audit_auditor, width="100%"),
                                    spacing="1"
                                ),
                                rx.vstack(
                                    rx.text("Start Date", font_size="13px", color="#64748b"),
                                    rx.input(placeholder="YYYY-MM-DD", value=AuditManagementState.new_audit_start, on_change=AuditManagementState.set_new_audit_start, width="100%"),
                                    spacing="1"
                                ),
                                rx.vstack(
                                    rx.text("End Date", font_size="13px", color="#64748b"),
                                    rx.input(placeholder="YYYY-MM-DD", value=AuditManagementState.new_audit_end, on_change=AuditManagementState.set_new_audit_end, width="100%"),
                                    spacing="1"
                                ),
                                columns="3", spacing="4", width="100%"
                            ),
                            rx.vstack(
                                rx.text("Scope", font_size="13px", color="#64748b"),
                                rx.text_area(placeholder="Describe the audit scope...", value=AuditManagementState.new_audit_scope, on_change=AuditManagementState.set_new_audit_scope, width="100%"),
                                spacing="1"
                            ),
                            rx.callout(
                                "Controls already tested via CCF (with passing results) will be automatically excluded from the audit scope.",
                                icon="info",
                                color_scheme="blue",
                                size="1"
                            ),
                            rx.hstack(
                                rx.button("Create Audit Plan", on_click=AuditManagementState.create_audit, bg="#3b82f6", color="white", cursor="pointer"),
                                rx.button("Cancel", on_click=AuditManagementState.toggle_audit_form, variant="outline", cursor="pointer"),
                                spacing="3"
                            ),
                            spacing="4", width="100%"
                        ),
                        bg="#f8fafc", padding="24px", border_radius="12px", border="1px dashed #3b82f6", margin_bottom="20px"
                    ),
                    rx.fragment()
                ),
                
                # Audit List
                rx.cond(
                    AuditManagementState.audits.length() > 0,
                    rx.vstack(
                        rx.foreach(
                            AuditManagementState.audits,
                            lambda audit: rx.box(
                                rx.vstack(
                                    rx.hstack(
                                        rx.vstack(
                                            rx.hstack(
                                                rx.text(audit["name"], font_size="18px", font_weight="600", color="#0f172a"),
                                                rx.badge(audit["status"], color_scheme=rx.cond(audit["status"] == "Completed", "green", rx.cond(audit["status"] == "In Progress", "yellow", "blue"))),
                                                rx.badge(audit["framework"], color_scheme="purple", size="1"),
                                                spacing="3"
                                            ),
                                            rx.hstack(
                                                rx.text("Auditor: " + audit["auditor"].to_string(), font_size="13px", color="#64748b"),
                                                rx.text("Period: " + audit["start_date"].to_string() + " - " + audit["end_date"].to_string(), font_size="13px", color="#64748b"),
                                                rx.text("Findings: " + audit["findings_count"].to_string(), font_size="13px", color="#64748b"),
                                                spacing="4"
                                            ),
                                            rx.text(audit["scope"], font_size="14px", color="#475569", margin_top="4px"),
                                            align_items="start", flex="1"
                                        ),
                                        rx.vstack(
                                            rx.hstack(
                                                rx.button("Start", on_click=AuditManagementState.update_audit_status(audit["id"], "In Progress"), size="1", variant="outline", color_scheme="yellow", cursor="pointer"),
                                                rx.button("Complete", on_click=AuditManagementState.update_audit_status(audit["id"], "Completed"), size="1", variant="outline", color_scheme="green", cursor="pointer"),
                                                spacing="2"
                                            ),
                                            rx.button(
                                                rx.hstack(rx.icon("plus", size=14), rx.text("Add Finding", font_size="12px"), spacing="1"),
                                                on_click=AuditManagementState.toggle_finding_form(audit["id"]),
                                                size="1", variant="outline", color_scheme="red", cursor="pointer"
                                            ),
                                            spacing="2", align_items="end"
                                        ),
                                        width="100%", align_items="start"
                                    ),
                                    
                                    # Findings for this audit (show if selected)
                                    rx.cond(
                                        AuditManagementState.selected_audit_id == audit["id"],
                                        rx.cond(
                                            AuditManagementState.show_finding_form,
                                            rx.box(
                                                rx.vstack(
                                                    rx.text("Add Finding", font_size="16px", font_weight="600"),
                                                    rx.grid(
                                                        rx.vstack(
                                                            rx.text("Related Control", font_size="13px", color="#64748b"),
                                                            rx.select(AuditManagementState.control_options, value=AuditManagementState.new_finding_control, on_change=AuditManagementState.set_new_finding_control, placeholder="Select control...", width="100%"),
                                                            spacing="1"
                                                        ),
                                                        rx.vstack(
                                                            rx.text("Severity", font_size="13px", color="#64748b"),
                                                            rx.select(["Critical", "High", "Medium", "Low"], value=AuditManagementState.new_finding_severity, on_change=AuditManagementState.set_new_finding_severity, width="100%"),
                                                            spacing="1"
                                                        ),
                                                        columns="2", spacing="4", width="100%"
                                                    ),
                                                    rx.text_area(placeholder="Finding description...", value=AuditManagementState.new_finding_desc, on_change=AuditManagementState.set_new_finding_desc, width="100%"),
                                                    rx.text_area(placeholder="Recommended remediation...", value=AuditManagementState.new_finding_remediation, on_change=AuditManagementState.set_new_finding_remediation, width="100%"),
                                                    rx.grid(
                                                        rx.input(placeholder="Assigned to", value=AuditManagementState.new_finding_assigned, on_change=AuditManagementState.set_new_finding_assigned, width="100%"),
                                                        rx.input(placeholder="Due date (YYYY-MM-DD)", value=AuditManagementState.new_finding_due, on_change=AuditManagementState.set_new_finding_due, width="100%"),
                                                        columns="2", spacing="4", width="100%"
                                                    ),
                                                    rx.hstack(
                                                        rx.button("Save Finding", on_click=AuditManagementState.create_finding, bg="#ef4444", color="white", cursor="pointer"),
                                                        rx.button("Cancel", on_click=AuditManagementState.toggle_finding_form(""), variant="outline", cursor="pointer"),
                                                        spacing="3"
                                                    ),
                                                    spacing="3", width="100%"
                                                ),
                                                bg="#fef2f2", padding="16px", border_radius="8px", margin_top="12px", border="1px dashed #fca5a5"
                                            ),
                                            rx.fragment()
                                        ),
                                        rx.fragment()
                                    ),
                                    
                                    width="100%"
                                ),
                                bg="white", padding="20px", border_radius="12px", border="1px solid #e2e8f0", margin_bottom="12px",
                                _hover={"border_color": "#3b82f6"}
                            )
                        ),
                        width="100%"
                    ),
                    rx.center(
                        rx.vstack(
                            rx.icon("clipboard-list", size=48, color="#94a3b8"),
                            rx.text("No audits planned yet", font_size="16px", color="#64748b"),
                            rx.text("Click 'New Audit Plan' to get started", font_size="14px", color="#94a3b8"),
                            align_items="center", spacing="2"
                        ),
                        padding="60px"
                    )
                ),
                
                bg="white", padding="30px", border_radius="12px", border="1px solid #e2e8f0"
            ),
            
            spacing="6", width="100%"
        )
    )


# Audit Readiness Page
@rx.page(route="/audit-readiness", title="Audit Readiness - GRC Platform", on_load=AuditManagementState.load_audit_data)
def audit_readiness() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Audit Readiness", font_size="40px", font_weight="bold", color="#0f172a", margin_bottom="10px"),
            rx.text("Check your readiness for framework audits — controls tested via CCF are auto-covered", font_size="18px", color="#64748b", margin_bottom="30px"),
            
            # Framework Selector
            rx.box(
                rx.hstack(
                    rx.vstack(
                        rx.text("Select Framework", font_size="14px", font_weight="600", color="#374151"),
                        rx.select(
                            AuditManagementState.framework_options,
                            value=AuditManagementState.selected_readiness_fw,
                            on_change=AuditManagementState.set_selected_readiness_fw,
                            placeholder="Choose a framework to check readiness...",
                            width="400px"
                        ),
                        spacing="1", align_items="start"
                    ),
                    spacing="4", align_items="end"
                ),
                bg="white", padding="24px", border_radius="12px", border="1px solid #e2e8f0", margin_bottom="20px"
            ),
            
            # Readiness Summary
            rx.cond(
                AuditManagementState.selected_readiness_fw != "",
                rx.vstack(
                    # Summary bar
                    rx.box(
                        rx.hstack(
                            rx.icon("shield-check", size=22, color="#10b981"),
                            rx.text("Readiness Summary: ", font_size="16px", font_weight="600", color="#0f172a"),
                            rx.text(AuditManagementState.readiness_summary, font_size="15px", color="#374151"),
                            spacing="2", align_items="center"
                        ),
                        bg="#f0fdf4", padding="16px", border_radius="10px", border="1px solid #bbf7d0", margin_bottom="20px", width="100%"
                    ),
                    
                    # Legend
                    rx.hstack(
                        rx.hstack(rx.box(width="14px", height="14px", bg="#10b981", border_radius="3px"), rx.text("Covered by CCF Testing", font_size="13px", color="#374151"), spacing="2"),
                        rx.hstack(rx.box(width="14px", height="14px", bg="#3b82f6", border_radius="3px"), rx.text("Audited", font_size="13px", color="#374151"), spacing="2"),
                        rx.hstack(rx.box(width="14px", height="14px", bg="#ef4444", border_radius="3px"), rx.text("Needs Audit", font_size="13px", color="#374151"), spacing="2"),
                        spacing="6", margin_bottom="15px"
                    ),
                    
                    # Controls List
                    rx.box(
                        rx.foreach(
                            AuditManagementState.readiness_controls,
                            lambda ctrl_str: rx.box(
                                rx.hstack(
                                    rx.cond(
                                        ctrl_str.contains("COVERED"),
                                        rx.icon("check-circle", size=18, color="#10b981"),
                                        rx.cond(
                                            ctrl_str.contains("AUDITED"),
                                            rx.icon("check-circle", size=18, color="#3b82f6"),
                                            rx.icon("alert-circle", size=18, color="#ef4444")
                                        )
                                    ),
                                    rx.text(ctrl_str, font_size="14px", color="#374151"),
                                    spacing="3", align_items="center"
                                ),
                                padding="12px 16px",
                                bg=rx.cond(
                                    ctrl_str.contains("COVERED"),
                                    "#f0fdf4",
                                    rx.cond(
                                        ctrl_str.contains("AUDITED"),
                                        "#eff6ff",
                                        "#fef2f2"
                                    )
                                ),
                                border_radius="8px",
                                border=rx.cond(
                                    ctrl_str.contains("COVERED"),
                                    "1px solid #bbf7d0",
                                    rx.cond(
                                        ctrl_str.contains("AUDITED"),
                                        "1px solid #bfdbfe",
                                        "1px solid #fecaca"
                                    )
                                ),
                                margin_bottom="8px"
                            )
                        ),
                        bg="white", padding="24px", border_radius="12px", border="1px solid #e2e8f0"
                    ),
                    
                    width="100%"
                ),
                rx.center(
                    rx.vstack(
                        rx.icon("shield", size=48, color="#94a3b8"),
                        rx.text("Select a framework to check audit readiness", font_size="16px", color="#64748b"),
                        align_items="center", spacing="2"
                    ),
                    padding="60px", bg="white", border_radius="12px", border="1px solid #e2e8f0"
                )
            ),
            
            spacing="6", width="100%"
        )
    )


# Create main app
app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="blue",
    )
)
